#!/usr/bin/env python3
"""Extract consistent face-zone crops from avatar stills."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = ROOT / "06_analysis" / "crops"

# Relative boxes for the current close-up grooming portrait frame: left, top, right, bottom.
DEFAULT_ZONES = {
    "skin_forehead": (0.36, 0.34, 0.66, 0.47),
    "skin_cheeks": (0.20, 0.58, 0.82, 0.73),
    "eyes": (0.18, 0.43, 0.76, 0.57),
    "lips": (0.35, 0.70, 0.66, 0.80),
    "hair_beard": (0.25, 0.64, 0.78, 0.90),
}


def load_pillow():
    try:
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError(
            "Pillow is required to extract crops. "
            "Install project dependencies with: pip install -r requirements.txt"
        ) from exc
    return Image


def resolve_input(path: Path) -> Path:
    if path.is_absolute():
        return path
    return ROOT / path


def parse_zone(value: str) -> tuple[str, tuple[float, float, float, float]]:
    try:
        name, coords = value.split("=", 1)
        numbers = tuple(float(part.strip()) for part in coords.split(","))
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "Zone must use format name=left,top,right,bottom with relative values from 0 to 1."
        ) from exc

    if len(numbers) != 4:
        raise argparse.ArgumentTypeError("Zone must contain exactly four coordinates.")

    left, top, right, bottom = numbers
    if not (0 <= left < right <= 1 and 0 <= top < bottom <= 1):
        raise argparse.ArgumentTypeError("Zone coordinates must satisfy 0 <= left < right <= 1 and 0 <= top < bottom <= 1.")

    clean_name = name.strip()
    if not clean_name:
        raise argparse.ArgumentTypeError("Zone name cannot be empty.")

    return clean_name, (left, top, right, bottom)


def relative_box_to_pixels(box: tuple[float, float, float, float], width: int, height: int) -> tuple[int, int, int, int]:
    left, top, right, bottom = box
    return (
        max(0, round(left * width)),
        max(0, round(top * height)),
        min(width, round(right * width)),
        min(height, round(bottom * height)),
    )


def image_label(path: Path) -> str:
    parent = path.parent.name
    stem = path.stem
    if parent in {"selected", "final_stills", "candidates"}:
        return stem
    return f"{parent}_{stem}"


def write_manifest(rows: list[dict[str, str]], output_path: Path) -> None:
    columns = ["avatar_id", "image_label", "zone", "source_file", "crop_file", "box_pixels", "box_relative"]
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def extract_crops(
    avatar_id: str,
    image_paths: list[Path],
    zones: dict[str, tuple[float, float, float, float]],
    output_dir: Path,
    overwrite: bool,
) -> list[dict[str, str]]:
    Image = load_pillow()
    manifest_rows = []

    avatar_output_dir = output_dir / avatar_id
    avatar_output_dir.mkdir(parents=True, exist_ok=True)

    for image_path in image_paths:
        label = image_label(image_path)
        with Image.open(image_path) as image:
            image = image.convert("RGB")
            width, height = image.size

            for zone_name, relative_box in zones.items():
                pixel_box = relative_box_to_pixels(relative_box, width, height)
                crop_path = avatar_output_dir / f"{label}_{zone_name}.jpg"

                if crop_path.exists() and not overwrite:
                    raise FileExistsError(f"Crop already exists: {crop_path.relative_to(ROOT)}. Use --overwrite to replace it.")

                crop = image.crop(pixel_box)
                crop.save(crop_path, quality=94)

                manifest_rows.append(
                    {
                        "avatar_id": avatar_id,
                        "image_label": label,
                        "zone": zone_name,
                        "source_file": image_path.relative_to(ROOT).as_posix(),
                        "crop_file": crop_path.relative_to(ROOT).as_posix(),
                        "box_pixels": ",".join(str(value) for value in pixel_box),
                        "box_relative": ",".join(f"{value:.4f}" for value in relative_box),
                    }
                )

    manifest_path = avatar_output_dir / "crop_manifest.csv"
    write_manifest(manifest_rows, manifest_path)
    return manifest_rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract face-zone crops for avatar realism analysis.")
    parser.add_argument("--avatar-id", required=True, help="Avatar ID, for example avatar_a_mens_grooming.")
    parser.add_argument("--images", nargs="+", type=Path, required=True, help="Input image paths.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Output crop directory.")
    parser.add_argument("--zone", action="append", type=parse_zone, help="Override/add zone: name=left,top,right,bottom.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing crop files.")
    args = parser.parse_args()

    image_paths = [resolve_input(path) for path in args.images]
    missing = [path for path in image_paths if not path.is_file()]
    if missing:
        print("ERROR: missing input images:", file=sys.stderr)
        for path in missing:
            print(f"- {path}", file=sys.stderr)
        return 1

    zones = dict(DEFAULT_ZONES)
    if args.zone:
        zones = {name: box for name, box in args.zone}

    output_dir = args.output_dir if args.output_dir.is_absolute() else ROOT / args.output_dir

    try:
        rows = extract_crops(args.avatar_id, image_paths, zones, output_dir, args.overwrite)
    except (OSError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Crops created: {len(rows)}")
    print(f"Output directory: {(output_dir / args.avatar_id).relative_to(ROOT)}")
    print(f"Zones: {', '.join(zones)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

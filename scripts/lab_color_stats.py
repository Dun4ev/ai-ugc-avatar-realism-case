#!/usr/bin/env python3
"""Calculate simple color and tone statistics for crop images."""

from __future__ import annotations

import argparse
import colorsys
import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CROP_ROOT = ROOT / "06_analysis" / "crops"
DEFAULT_OUTPUT_ROOT = ROOT / "06_analysis" / "lab_color_stats"


def load_dependencies():
    try:
        import numpy as np
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError(
            "Pillow and NumPy are required for color stats. "
            "Install project dependencies with: pip install -r requirements.txt"
        ) from exc
    return np, Image


def parse_crop_name(path: Path) -> tuple[str, str]:
    stem = path.stem
    if stem.startswith("final_realism_001_"):
        return "final_realism_001", stem.removeprefix("final_realism_001_")
    if "_" not in stem:
        return stem, ""
    label, zone = stem.split("_", 1)
    return label, zone


def image_stats(path: Path) -> dict[str, str]:
    np, Image = load_dependencies()
    with Image.open(path) as image:
        rgb = np.asarray(image.convert("RGB"), dtype=np.float32) / 255.0

    red = rgb[:, :, 0]
    green = rgb[:, :, 1]
    blue = rgb[:, :, 2]
    luminance = 0.2126 * red + 0.7152 * green + 0.0722 * blue
    max_channel = rgb.max(axis=2)
    min_channel = rgb.min(axis=2)
    chroma_proxy = max_channel - min_channel

    flat = rgb.reshape(-1, 3)
    hsv = np.array([colorsys.rgb_to_hsv(*pixel) for pixel in flat], dtype=np.float32)
    hue = hsv[:, 0]
    saturation = hsv[:, 1]
    value = hsv[:, 2]

    return {
        "width": str(rgb.shape[1]),
        "height": str(rgb.shape[0]),
        "mean_r": f"{red.mean():.4f}",
        "mean_g": f"{green.mean():.4f}",
        "mean_b": f"{blue.mean():.4f}",
        "mean_luminance": f"{luminance.mean():.4f}",
        "std_luminance": f"{luminance.std():.4f}",
        "mean_hue": f"{hue.mean():.4f}",
        "mean_saturation": f"{saturation.mean():.4f}",
        "mean_value": f"{value.mean():.4f}",
        "mean_chroma_proxy": f"{chroma_proxy.mean():.4f}",
        "p05_luminance": f"{float(np.percentile(luminance, 5)):.4f}",
        "p95_luminance": f"{float(np.percentile(luminance, 95)):.4f}",
    }


def discover_crops(crop_dir: Path) -> list[Path]:
    return sorted(path for path in crop_dir.glob("*.jpg") if path.is_file())


def write_stats(rows: list[dict[str, str]], output_path: Path) -> None:
    columns = [
        "avatar_id",
        "image_label",
        "zone",
        "crop_file",
        "width",
        "height",
        "mean_r",
        "mean_g",
        "mean_b",
        "mean_luminance",
        "std_luminance",
        "mean_hue",
        "mean_saturation",
        "mean_value",
        "mean_chroma_proxy",
        "p05_luminance",
        "p95_luminance",
    ]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Calculate color/tone stats for crop images.")
    parser.add_argument("--avatar-id", required=True, help="Avatar ID.")
    parser.add_argument("--crop-dir", type=Path, help="Directory with crop JPG files.")
    parser.add_argument("--output", type=Path, help="Output CSV path.")
    args = parser.parse_args()

    crop_dir = args.crop_dir
    if crop_dir is None:
        crop_dir = DEFAULT_CROP_ROOT / args.avatar_id
    elif not crop_dir.is_absolute():
        crop_dir = ROOT / crop_dir

    output_path = args.output
    if output_path is None:
        output_path = DEFAULT_OUTPUT_ROOT / f"{args.avatar_id}_color_stats.csv"
    elif not output_path.is_absolute():
        output_path = ROOT / output_path

    if not crop_dir.is_dir():
        print(f"ERROR: crop directory not found: {crop_dir}", file=sys.stderr)
        return 1

    rows = []
    for crop_path in discover_crops(crop_dir):
        image_label, zone = parse_crop_name(crop_path)
        stats = image_stats(crop_path)
        rows.append(
            {
                "avatar_id": args.avatar_id,
                "image_label": image_label,
                "zone": zone,
                "crop_file": crop_path.relative_to(ROOT).as_posix(),
                **stats,
            }
        )

    if not rows:
        print(f"ERROR: no crop JPG files found in {crop_dir.relative_to(ROOT)}", file=sys.stderr)
        return 1

    write_stats(rows, output_path)
    print(f"Color stats written: {output_path.relative_to(ROOT)}")
    print(f"Crops analyzed: {len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

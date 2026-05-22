#!/usr/bin/env python3
"""Create a zone-by-zone crop comparison grid from crop_manifest.csv."""

from __future__ import annotations

import argparse
import csv
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CROP_ROOT = ROOT / "06_analysis" / "crops"
ANALYSIS_OUTPUT_DIR = ROOT / "06_analysis" / "comparison_grids"
REPORT_OUTPUT_DIR = ROOT / "07_report" / "assets" / "images"

DEFAULT_ZONES = ["skin_forehead", "skin_cheeks", "eyes", "lips", "hair_beard"]


def load_pillow():
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError as exc:
        raise RuntimeError(
            "Pillow is required to create crop comparison grids. "
            "Install project dependencies with: pip install -r requirements.txt"
        ) from exc
    return Image, ImageDraw, ImageFont


def read_manifest(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Crop manifest not found: {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def ensure_can_write(path: Path, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Output already exists: {path.relative_to(ROOT)}. Use --overwrite to replace it.")


def fit_to_box(image, width: int, height: int):
    image = image.convert("RGB")
    image.thumbnail((width, height))
    return image


def draw_centered(draw, text: str, box: tuple[int, int, int, int], font, fill) -> None:
    left, top, right, bottom = box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = left + max(0, (right - left - text_width) // 2)
    y = top + max(0, (bottom - top - text_height) // 2)
    draw.text((x, y), text, font=font, fill=fill)


def manifest_index(rows: list[dict[str, str]]) -> dict[tuple[str, str], Path]:
    indexed = {}
    for row in rows:
        key = (row["image_label"], row["zone"])
        indexed[key] = ROOT / row["crop_file"]
    return indexed


def create_grid(
    avatar_id: str,
    manifest_path: Path,
    before_label: str,
    after_label: str,
    zones: list[str],
    output_name: str,
    overwrite: bool,
) -> tuple[Path, Path]:
    Image, ImageDraw, ImageFont = load_pillow()
    rows = read_manifest(manifest_path)
    crops = manifest_index(rows)

    missing = []
    for zone in zones:
        for label in (before_label, after_label):
            path = crops.get((label, zone))
            if not path or not path.is_file():
                missing.append(f"{label}/{zone}")
    if missing:
        raise FileNotFoundError("Missing crops: " + ", ".join(missing))

    if not output_name.lower().endswith((".jpg", ".jpeg", ".png")):
        output_name = f"{output_name}.jpg"

    analysis_output = ANALYSIS_OUTPUT_DIR / output_name
    report_output = REPORT_OUTPUT_DIR / output_name
    ensure_can_write(analysis_output, overwrite)
    ensure_can_write(report_output, overwrite)

    label_width = 180
    cell_width = 420
    cell_height = 220
    header_height = 58
    padding = 16
    columns = [before_label, after_label]

    canvas_width = label_width + len(columns) * cell_width
    canvas_height = header_height + len(zones) * cell_height
    canvas = Image.new("RGB", (canvas_width, canvas_height), "white")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()

    draw.rectangle([0, 0, canvas_width - 1, canvas_height - 1], outline=(210, 210, 210), width=1)
    draw_centered(draw, avatar_id, (0, 0, label_width, header_height), font, (35, 35, 35))
    for col_index, label in enumerate(columns):
        x0 = label_width + col_index * cell_width
        draw_centered(draw, label, (x0, 0, x0 + cell_width, header_height), font, (35, 35, 35))

    for row_index, zone in enumerate(zones):
        y0 = header_height + row_index * cell_height
        draw_centered(draw, zone, (0, y0, label_width, y0 + cell_height), font, (35, 35, 35))

        for col_index, label in enumerate(columns):
            x0 = label_width + col_index * cell_width
            crop_path = crops[(label, zone)]
            with Image.open(crop_path) as image:
                fitted = fit_to_box(image, cell_width - padding * 2, cell_height - padding * 2)
            paste_x = x0 + padding + (cell_width - padding * 2 - fitted.width) // 2
            paste_y = y0 + padding + (cell_height - padding * 2 - fitted.height) // 2
            canvas.paste(fitted, (paste_x, paste_y))
            draw.rectangle([x0, y0, x0 + cell_width, y0 + cell_height], outline=(230, 230, 230), width=1)

    analysis_output.parent.mkdir(parents=True, exist_ok=True)
    report_output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(analysis_output, quality=92)
    shutil.copy2(analysis_output, report_output)
    return analysis_output, report_output


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a crop comparison grid from crop_manifest.csv.")
    parser.add_argument("--avatar-id", required=True, help="Avatar ID.")
    parser.add_argument("--before-label", default="base", help="Manifest image_label for the left column.")
    parser.add_argument("--after-label", default="final_realism_001", help="Manifest image_label for the right column.")
    parser.add_argument("--manifest", type=Path, help="Path to crop_manifest.csv.")
    parser.add_argument("--zones", nargs="+", default=DEFAULT_ZONES, help="Zones to include, in order.")
    parser.add_argument("--output-name", help="Output filename.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing output files.")
    args = parser.parse_args()

    manifest_path = args.manifest
    if manifest_path is None:
        manifest_path = DEFAULT_CROP_ROOT / args.avatar_id / "crop_manifest.csv"
    elif not manifest_path.is_absolute():
        manifest_path = ROOT / manifest_path

    output_name = args.output_name or f"{args.avatar_id}_crop_comparison_001.jpg"

    try:
        analysis_output, report_output = create_grid(
            args.avatar_id,
            manifest_path,
            args.before_label,
            args.after_label,
            args.zones,
            output_name,
            args.overwrite,
        )
    except (OSError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Crop comparison grid created: {analysis_output.relative_to(ROOT)}")
    print(f"Copied to report assets: {report_output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

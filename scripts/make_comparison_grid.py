#!/usr/bin/env python3
"""Create a 2- or 3-column comparison grid for avatar outputs."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS_OUTPUT_DIR = ROOT / "06_analysis" / "comparison_grids"
REPORT_OUTPUT_DIR = ROOT / "07_report" / "assets" / "images"

DEFAULT_LABELS = ["Base avatar", "Realism pass", "Final still"]


def load_pillow():
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError as exc:
        raise RuntimeError(
            "Pillow is required to create comparison grids. "
            "Install project dependencies with: pip install -r requirements.txt"
        ) from exc
    return Image, ImageDraw, ImageFont


def resolve_input(path: Path) -> Path:
    if path.is_absolute():
        return path
    return ROOT / path


def output_name(avatar_id: str, output_name_arg: str | None) -> str:
    if output_name_arg:
        name = output_name_arg
    else:
        name = f"{avatar_id}_comparison_001.jpg"
    return name if name.lower().endswith((".jpg", ".jpeg", ".png")) else f"{name}.jpg"


def ensure_can_write(path: Path, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Output already exists: {path.relative_to(ROOT)}. Use --overwrite to replace it.")


def draw_centered_text(draw, text: str, box: tuple[int, int, int, int], font, fill) -> None:
    left, top, right, bottom = box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = left + max(0, (right - left - text_width) // 2)
    y = top + max(0, (bottom - top - text_height) // 2)
    draw.text((x, y), text, font=font, fill=fill)


def fit_image(image, target_width: int, target_height: int):
    image = image.convert("RGB")
    image.thumbnail((target_width, target_height))
    return image


def create_grid(
    image_paths: list[Path],
    labels: list[str],
    output_path: Path,
    width: int,
    height: int,
) -> None:
    Image, ImageDraw, ImageFont = load_pillow()

    columns = len(image_paths)
    padding = 24
    label_height = 48
    cell_width = width
    cell_height = height + label_height + padding * 2

    canvas = Image.new("RGB", (columns * cell_width, cell_height), "white")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()

    for index, image_path in enumerate(image_paths):
        x0 = index * cell_width
        with Image.open(image_path) as source:
            image = fit_image(source, width - padding * 2, height)

        image_x = x0 + padding + (width - padding * 2 - image.width) // 2
        image_y = padding + (height - image.height) // 2
        canvas.paste(image, (image_x, image_y))

        draw.rectangle(
            [
                x0 + padding,
                padding,
                x0 + width - padding,
                padding + height,
            ],
            outline=(215, 215, 215),
            width=1,
        )
        draw_centered_text(
            draw,
            labels[index],
            (x0 + padding, padding + height, x0 + width - padding, cell_height - padding),
            font,
            fill=(35, 35, 35),
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path, quality=92)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a labeled comparison grid for avatar images.")
    parser.add_argument("--avatar-id", required=True, help="Avatar ID, for example avatar_a_mens_grooming.")
    parser.add_argument("--images", nargs="+", type=Path, required=True, help="Two or three input image paths.")
    parser.add_argument("--labels", nargs="+", help="Optional labels. Must match the number of images.")
    parser.add_argument("--output-name", help="Optional output filename. Defaults to <avatar_id>_comparison_001.jpg.")
    parser.add_argument("--width", type=int, default=420, help="Column image area width in pixels.")
    parser.add_argument("--height", type=int, default=560, help="Column image area height in pixels.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing output files.")
    args = parser.parse_args()

    if len(args.images) not in (2, 3):
        print("ERROR: --images must contain exactly 2 or 3 paths.", file=sys.stderr)
        return 1

    labels = args.labels if args.labels else DEFAULT_LABELS[: len(args.images)]
    if len(labels) != len(args.images):
        print("ERROR: --labels must match the number of input images.", file=sys.stderr)
        return 1

    if args.width < 160 or args.height < 160:
        print("ERROR: --width and --height must be at least 160.", file=sys.stderr)
        return 1

    image_paths = [resolve_input(path) for path in args.images]
    missing = [path for path in image_paths if not path.is_file()]
    if missing:
        print("ERROR: missing input images:", file=sys.stderr)
        for path in missing:
            print(f"- {path}", file=sys.stderr)
        return 1

    name = output_name(args.avatar_id, args.output_name)
    analysis_output = ANALYSIS_OUTPUT_DIR / name
    report_output = REPORT_OUTPUT_DIR / name

    try:
        ensure_can_write(analysis_output, args.overwrite)
        ensure_can_write(report_output, args.overwrite)
        create_grid(image_paths, labels, analysis_output, args.width, args.height)
        report_output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(analysis_output, report_output)
    except (OSError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Comparison grid created: {analysis_output.relative_to(ROOT)}")
    print(f"Copied to report assets: {report_output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

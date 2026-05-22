#!/usr/bin/env python3
"""Create a contact sheet from registered source images."""

from __future__ import annotations

import argparse
import csv
import sys
from math import ceil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "02_source_data" / "dataset_register.csv"
DEFAULT_OUTPUT = ROOT / "06_analysis" / "contact_sheets" / "contact_sheet_001.jpg"

HEADER = [
    "image_id",
    "source",
    "license_note",
    "filename",
    "relative_path",
    "subject_type",
    "skin_tone",
    "lighting",
    "crop_type",
    "use_case",
    "allowed_for_public_report",
    "notes",
]


def read_rows() -> list[dict[str, str]]:
    if not REGISTER_PATH.exists():
        raise FileNotFoundError(f"Dataset register not found: {REGISTER_PATH.relative_to(ROOT)}")

    with REGISTER_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != HEADER:
            raise ValueError(
                f"Invalid CSV header in {REGISTER_PATH.relative_to(ROOT)}. "
                f"Expected: {HEADER}. Actual: {reader.fieldnames}"
            )
        return [{column: row.get(column, "").strip() for column in HEADER} for row in reader]


def is_selected(row: dict[str, str]) -> bool:
    return row["allowed_for_public_report"].lower() == "yes" or bool(row["use_case"])


def selected_existing_rows(rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[str]]:
    selected = []
    missing = []

    for row in rows:
        if not is_selected(row):
            continue

        path = ROOT / row["relative_path"]
        if path.is_file():
            selected.append(row)
        else:
            missing.append(row["relative_path"])

    return selected, missing


def text_lines(row: dict[str, str]) -> list[str]:
    return [
        row["image_id"] or "no image_id",
        f"source: {row['source'] or '-'}",
        f"skin: {row['skin_tone'] or '-'}",
        f"light: {row['lighting'] or '-'}",
        f"use: {row['use_case'] or '-'}",
    ]


def load_pillow():
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError as exc:
        raise RuntimeError(
            "Pillow is required to create contact sheets. "
            "Install project dependencies with: pip install -r requirements.txt"
        ) from exc
    return Image, ImageDraw, ImageFont


def draw_wrapped_text(draw, xy: tuple[int, int], text: str, font, fill, max_width: int) -> int:
    x, y = xy
    words = text.split()
    if not words:
        return y

    line = words[0]
    for word in words[1:]:
        candidate = f"{line} {word}"
        if draw.textbbox((0, 0), candidate, font=font)[2] <= max_width:
            line = candidate
        else:
            draw.text((x, y), line, font=font, fill=fill)
            y += 16
            line = word

    draw.text((x, y), line, font=font, fill=fill)
    return y + 16


def create_contact_sheet(
    rows: list[dict[str, str]],
    output_path: Path,
    columns: int,
    thumb_size: int,
) -> None:
    Image, ImageDraw, ImageFont = load_pillow()

    rows_count = ceil(len(rows) / columns)
    padding = 18
    label_height = 94
    cell_width = thumb_size + padding * 2
    cell_height = thumb_size + label_height + padding * 2

    sheet = Image.new("RGB", (columns * cell_width, rows_count * cell_height), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()

    for index, row in enumerate(rows):
        column = index % columns
        row_index = index // columns
        cell_x = column * cell_width
        cell_y = row_index * cell_height

        image_path = ROOT / row["relative_path"]
        with Image.open(image_path) as image:
            image = image.convert("RGB")
            image.thumbnail((thumb_size, thumb_size))
            image_x = cell_x + padding + (thumb_size - image.width) // 2
            image_y = cell_y + padding + (thumb_size - image.height) // 2
            sheet.paste(image, (image_x, image_y))

        draw.rectangle(
            [
                cell_x + padding,
                cell_y + padding,
                cell_x + padding + thumb_size,
                cell_y + padding + thumb_size,
            ],
            outline=(215, 215, 215),
            width=1,
        )

        text_y = cell_y + padding + thumb_size + 10
        for line in text_lines(row):
            text_y = draw_wrapped_text(
                draw,
                (cell_x + padding, text_y),
                line,
                font,
                fill=(35, 35, 35),
                max_width=thumb_size,
            )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output_path, quality=92)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a contact sheet from dataset_register.csv.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output JPG path.")
    parser.add_argument("--columns", type=int, default=4, help="Number of grid columns.")
    parser.add_argument("--thumb-size", type=int, default=220, help="Thumbnail size in pixels.")
    args = parser.parse_args()

    if args.columns < 1:
        print("ERROR: --columns must be at least 1.", file=sys.stderr)
        return 1
    if args.thumb_size < 80:
        print("ERROR: --thumb-size must be at least 80.", file=sys.stderr)
        return 1

    rows = read_rows()
    selected, missing = selected_existing_rows(rows)

    if missing:
        print("WARNING: selected rows with missing files:")
        for path in missing:
            print(f"- {path}")

    if not selected:
        print("No eligible images found.")
        print("Select rows by setting allowed_for_public_report=yes or filling use_case.")
        return 0

    output_path = args.output
    if not output_path.is_absolute():
        output_path = ROOT / output_path

    create_contact_sheet(selected, output_path, args.columns, args.thumb_size)
    print(f"Contact sheet created: {output_path.relative_to(ROOT)}")
    print(f"Images included: {len(selected)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

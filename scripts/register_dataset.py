#!/usr/bin/env python3
"""Register source images in 02_source_data/dataset_register.csv."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "02_source_data"
REGISTER_PATH = SOURCE_ROOT / "dataset_register.csv"

SCAN_DIRS = [
    SOURCE_ROOT / "public_references",
    SOURCE_ROOT / "generated_references",
    SOURCE_ROOT / "own_test_images",
]

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

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


def slug(value: str) -> str:
    normalized = value.lower()
    normalized = re.sub(r"[^a-z0-9]+", "_", normalized)
    return normalized.strip("_") or "image"


def relative_to_root(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def source_from_path(path: Path) -> str:
    relative = path.relative_to(SOURCE_ROOT)
    parts = relative.parts
    if parts[0] == "public_references" and len(parts) > 1:
        return parts[1]
    return parts[0]


def image_id_for(path: Path) -> str:
    relative = path.relative_to(SOURCE_ROOT)
    stem = slug(path.stem)

    if relative.parts[0] == "public_references" and len(relative.parts) > 1:
        prefix = f"public_{slug(relative.parts[1])}"
    else:
        prefix = slug(relative.parts[0])

    return f"{prefix}_{stem}"


def discover_images() -> list[Path]:
    images = []
    for directory in SCAN_DIRS:
        if not directory.exists():
            continue
        for path in directory.rglob("*"):
            if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
                images.append(path)
    return sorted(images, key=lambda item: item.relative_to(ROOT).as_posix().lower())


def read_existing_rows() -> list[dict[str, str]]:
    if not REGISTER_PATH.exists():
        return []

    with REGISTER_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != HEADER:
            raise ValueError(
                f"Invalid CSV header in {relative_to_root(REGISTER_PATH)}. "
                f"Expected: {HEADER}. Actual: {reader.fieldnames}"
            )
        return [{column: row.get(column, "") for column in HEADER} for row in reader]


def write_rows(rows: list[dict[str, str]]) -> None:
    REGISTER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with REGISTER_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(rows)


def build_row(path: Path) -> dict[str, str]:
    return {
        "image_id": image_id_for(path),
        "source": source_from_path(path),
        "license_note": "",
        "filename": path.name,
        "relative_path": relative_to_root(path),
        "subject_type": "",
        "skin_tone": "",
        "lighting": "",
        "crop_type": "",
        "use_case": "",
        "allowed_for_public_report": "",
        "notes": "",
    }


def update_register(dry_run: bool = False) -> tuple[int, int, int]:
    rows = read_existing_rows()
    existing_by_path = {row["relative_path"]: row for row in rows if row["relative_path"]}
    existing_ids = {row["image_id"] for row in rows if row["image_id"]}

    images = discover_images()
    added_rows = []

    for image in images:
        relative_path = relative_to_root(image)
        if relative_path in existing_by_path:
            continue

        row = build_row(image)
        base_id = row["image_id"]
        counter = 2
        while row["image_id"] in existing_ids:
            row["image_id"] = f"{base_id}_{counter}"
            counter += 1
        existing_ids.add(row["image_id"])
        added_rows.append(row)

    if added_rows and not dry_run:
        write_rows(rows + added_rows)
    elif not REGISTER_PATH.exists() and not dry_run:
        write_rows(rows)

    return len(images), len(added_rows), len(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Register source images in dataset_register.csv.")
    parser.add_argument("--dry-run", action="store_true", help="Scan and report without writing changes.")
    args = parser.parse_args()

    images_found, rows_added, rows_preserved = update_register(dry_run=args.dry_run)

    prefix = "DRY RUN: " if args.dry_run else ""
    print(f"{prefix}images found: {images_found}")
    print(f"{prefix}rows added: {rows_added}")
    print(f"{prefix}rows preserved: {rows_preserved}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

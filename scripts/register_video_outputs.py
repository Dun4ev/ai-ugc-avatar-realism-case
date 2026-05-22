#!/usr/bin/env python3
"""Register generated video outputs and copy them into report assets."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VIDEO_LOG = ROOT / "05_video_tests" / "video_test_log.csv"
REPORT_VIDEO_DIR = ROOT / "07_report" / "assets" / "video"

VIDEO_LOG_COLUMNS = [
    "video_run_id",
    "avatar_id",
    "input_still",
    "tool_used",
    "prompt_file",
    "output_video",
    "duration_sec",
    "face_stability",
    "eye_stability",
    "lips_stability",
    "skin_stability",
    "identity_consistency",
    "overall_score",
    "verdict",
    "notes",
]


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_rows() -> list[dict[str, str]]:
    with VIDEO_LOG.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_rows(rows: list[dict[str, str]]) -> None:
    with VIDEO_LOG.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=VIDEO_LOG_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def expected_output(row: dict[str, str]) -> Path:
    return ROOT / "05_video_tests" / row["avatar_id"] / "video_outputs" / f"{row['video_run_id']}.mp4"


def ffprobe_duration(path: Path) -> str:
    try:
        result = subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "json",
                str(path),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return ""

    data = json.loads(result.stdout)
    duration = float(data.get("format", {}).get("duration", 0))
    return f"{duration:.2f}" if duration else ""


def register_outputs(tool_used: str, overwrite_assets: bool) -> list[dict[str, str]]:
    rows = read_rows()
    registered = []
    REPORT_VIDEO_DIR.mkdir(parents=True, exist_ok=True)

    for row in rows:
        output_path = expected_output(row)
        if not output_path.is_file():
            continue

        asset_path = REPORT_VIDEO_DIR / output_path.name
        if asset_path.exists() and not overwrite_assets:
            raise FileExistsError(f"Report video asset exists: {relative(asset_path)}. Use --overwrite-assets.")
        shutil.copy2(output_path, asset_path)

        row["tool_used"] = tool_used
        row["output_video"] = relative(output_path)
        row["duration_sec"] = ffprobe_duration(output_path)
        row["verdict"] = "pending_review"
        row["notes"] = "Video output registered; stability scores pending user review."
        registered.append(row)

    write_rows(rows)
    return registered


def main() -> int:
    parser = argparse.ArgumentParser(description="Register generated mp4 outputs in video_test_log.csv.")
    parser.add_argument("--tool-used", default="external_image_to_video_tool_unspecified", help="Tool name to write into the video log.")
    parser.add_argument("--overwrite-assets", action="store_true", help="Overwrite copied report video assets.")
    args = parser.parse_args()

    if not VIDEO_LOG.is_file():
        print(f"ERROR: missing video log: {relative(VIDEO_LOG)}", file=sys.stderr)
        return 1

    try:
        registered = register_outputs(args.tool_used, args.overwrite_assets)
    except OSError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if not registered:
        print("No generated video outputs found.")
        return 1

    for row in registered:
        print(f"Registered {row['video_run_id']}: {row['output_video']} duration={row['duration_sec']}")
    print(f"Copied report assets to: {relative(REPORT_VIDEO_DIR)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

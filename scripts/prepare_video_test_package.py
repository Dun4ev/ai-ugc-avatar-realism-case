#!/usr/bin/env python3
"""Prepare traceable image-to-video test inputs without generating videos."""

from __future__ import annotations

import argparse
import csv
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VIDEO_LOG = ROOT / "05_video_tests" / "video_test_log.csv"

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


PROMPT_TEMPLATES = {
    "avatar_a_mens_grooming": """# Video Test Prompt: Avatar A

## Цель

Проверить, сохраняется ли реалистичность men's grooming portrait при коротком image-to-video движении.

## Input still

`05_video_tests/avatar_a_mens_grooming/input_stills/avatar_a_realism_001_input.jpg`

## Prompt EN

Close-up UGC skincare and grooming video of the same man, subtle natural head movement, slight eye movement, relaxed confident expression, realistic skin texture, stable beard and lips, soft studio lighting, no product shown, no text, no logo.

## Negative constraints

- Do not change identity.
- Do not change beard shape.
- Do not add product packaging.
- Do not add text, subtitles, watermark, logo or brand.
- Avoid exaggerated facial motion.
- Avoid waxy skin, unstable eyes, teeth deformation and lip warping.

## План оценки

После генерации оценить по шкале 1-5:

- face_stability
- eye_stability
- lips_stability
- skin_stability
- identity_consistency
- overall_score
""",
    "avatar_b_skincare_creator": """# Video Test Prompt: Avatar B

## Цель

Проверить, сохраняется ли реалистичность skincare close-up portrait при коротком image-to-video движении.

## Input still

`05_video_tests/avatar_b_skincare_creator/input_stills/avatar_b_realism_001_input.jpg`

## Prompt EN

Close-up UGC skincare routine video of the same woman, subtle natural head movement, soft eye movement, calm premium beauty expression, realistic skin texture, stable lips and hairline, soft studio lighting, no product shown, no text, no logo.

## Negative constraints

- Do not change identity.
- Do not change eye color or eye shape.
- Do not add product packaging.
- Do not add text, subtitles, watermark, logo or brand.
- Avoid exaggerated facial motion.
- Avoid waxy skin, unstable eyes, teeth deformation, lip warping and hairline flicker.

## План оценки

После генерации оценить по шкале 1-5:

- face_stability
- eye_stability
- lips_stability
- skin_stability
- identity_consistency
- overall_score
""",
}


DEFAULT_STILLS = {
    "avatar_a_mens_grooming": ROOT / "04_realism_passes" / "avatar_a_mens_grooming" / "final_stills" / "final_realism_001.jpg",
    "avatar_b_skincare_creator": ROOT / "04_realism_passes" / "avatar_b_skincare_creator" / "final_stills" / "final_realism_001.jpg",
}


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_log_rows() -> list[dict[str, str]]:
    if not VIDEO_LOG.exists():
        return []
    with VIDEO_LOG.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_log_rows(rows: list[dict[str, str]]) -> None:
    VIDEO_LOG.parent.mkdir(parents=True, exist_ok=True)
    with VIDEO_LOG.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=VIDEO_LOG_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def upsert_log_row(row: dict[str, str]) -> None:
    rows = read_log_rows()
    replaced = False
    for index, existing in enumerate(rows):
        if existing["video_run_id"] == row["video_run_id"]:
            rows[index] = row
            replaced = True
            break
    if not replaced:
        rows.append(row)
    write_log_rows(rows)


def prepare_avatar(avatar_id: str, overwrite: bool) -> tuple[Path, Path]:
    if avatar_id not in DEFAULT_STILLS:
        raise ValueError(f"Unsupported avatar_id: {avatar_id}")

    source_still = DEFAULT_STILLS[avatar_id]
    if not source_still.is_file():
        raise FileNotFoundError(f"Missing realism still: {relative(source_still)}")

    avatar_dir = ROOT / "05_video_tests" / avatar_id
    input_dir = avatar_dir / "input_stills"
    input_dir.mkdir(parents=True, exist_ok=True)

    short_id = "avatar_a" if avatar_id == "avatar_a_mens_grooming" else "avatar_b"
    input_still = input_dir / f"{short_id}_realism_001_input.jpg"
    prompt_file = avatar_dir / "prompt_video_001.md"

    if input_still.exists() and not overwrite:
        raise FileExistsError(f"Input still exists: {relative(input_still)}. Use --overwrite.")
    if prompt_file.exists() and not overwrite:
        raise FileExistsError(f"Prompt file exists: {relative(prompt_file)}. Use --overwrite.")

    shutil.copy2(source_still, input_still)
    prompt_file.write_text(PROMPT_TEMPLATES[avatar_id], encoding="utf-8")

    video_run_id = f"{short_id}_video_001"
    upsert_log_row(
        {
            "video_run_id": video_run_id,
            "avatar_id": avatar_id,
            "input_still": relative(input_still),
            "tool_used": "pending_tool_selection",
            "prompt_file": relative(prompt_file),
            "output_video": "",
            "duration_sec": "",
            "face_stability": "",
            "eye_stability": "",
            "lips_stability": "",
            "skin_stability": "",
            "identity_consistency": "",
            "overall_score": "",
            "verdict": "pending_generation",
            "notes": "Input still and prompt prepared; no video generated yet.",
        }
    )

    return input_still, prompt_file


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare image-to-video input stills, prompts and pending video log rows.")
    parser.add_argument("--avatar-id", choices=sorted(DEFAULT_STILLS), action="append", help="Avatar to prepare. Repeat for multiple.")
    parser.add_argument("--all", action="store_true", help="Prepare all supported avatars.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite prepared input stills and prompt files.")
    args = parser.parse_args()

    avatar_ids = sorted(DEFAULT_STILLS) if args.all else args.avatar_id
    if not avatar_ids:
        print("ERROR: use --all or at least one --avatar-id.", file=sys.stderr)
        return 1

    try:
        for avatar_id in avatar_ids:
            input_still, prompt_file = prepare_avatar(avatar_id, args.overwrite)
            print(f"Prepared {avatar_id}: {relative(input_still)}")
            print(f"Prompt: {relative(prompt_file)}")
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Video log updated: {relative(VIDEO_LOG)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

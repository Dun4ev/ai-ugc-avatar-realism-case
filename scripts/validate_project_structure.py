#!/usr/bin/env python3
"""Validate the initial AI UGC avatar realism project scaffold."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DIRS = [
    "00_project_control",
    "01_character_briefs/avatar_a_mens_grooming",
    "01_character_briefs/avatar_b_skincare_creator",
    "02_source_data/public_references/pexels_unsplash",
    "02_source_data/public_references/ppr10k_subset",
    "02_source_data/generated_references",
    "02_source_data/own_test_images",
    "03_base_avatars/avatar_a_mens_grooming/candidates",
    "03_base_avatars/avatar_a_mens_grooming/selected",
    "03_base_avatars/avatar_b_skincare_creator/candidates",
    "03_base_avatars/avatar_b_skincare_creator/selected",
    "04_realism_passes/avatar_a_mens_grooming/pass_01_skin",
    "04_realism_passes/avatar_a_mens_grooming/pass_02_eyes",
    "04_realism_passes/avatar_a_mens_grooming/pass_03_lips",
    "04_realism_passes/avatar_a_mens_grooming/pass_04_hair_beard",
    "04_realism_passes/avatar_a_mens_grooming/final_stills",
    "04_realism_passes/avatar_b_skincare_creator/pass_01_skin",
    "04_realism_passes/avatar_b_skincare_creator/pass_02_eyes",
    "04_realism_passes/avatar_b_skincare_creator/pass_03_lips",
    "04_realism_passes/avatar_b_skincare_creator/pass_04_hair",
    "04_realism_passes/avatar_b_skincare_creator/final_stills",
    "05_video_tests/avatar_a_mens_grooming/input_stills",
    "05_video_tests/avatar_a_mens_grooming/video_outputs",
    "05_video_tests/avatar_b_skincare_creator/input_stills",
    "05_video_tests/avatar_b_skincare_creator/video_outputs",
    "06_analysis/crops",
    "06_analysis/comparison_grids",
    "06_analysis/contact_sheets",
    "06_analysis/lab_color_stats",
    "07_report/assets/images",
    "07_report/assets/video",
    "07_report/assets/css",
    "08_site/assets",
    "09_workflows/comfyui",
    "scripts",
]

REQUIRED_FILES = [
    "PROJECT_BRIEF.md",
    "PROJECT_BRIEF_AI_UGC_AVATAR_REALISM.md",
    "AGENTS.md",
    "README.md",
    "requirements.txt",
    ".gitignore",
    "00_project_control/project_goal.md",
    "00_project_control/decisions.md",
    "00_project_control/open_questions.md",
    "00_project_control/roadmap.md",
    "00_project_control/references.md",
    "01_character_briefs/avatar_a_mens_grooming/character_brief.md",
    "01_character_briefs/avatar_a_mens_grooming/character_profile.json",
    "01_character_briefs/avatar_a_mens_grooming/prompt_history.md",
    "01_character_briefs/avatar_b_skincare_creator/character_brief.md",
    "01_character_briefs/avatar_b_skincare_creator/character_profile.json",
    "01_character_briefs/avatar_b_skincare_creator/prompt_history.md",
    "02_source_data/source_license_notes.md",
    "05_video_tests/avatar_a_mens_grooming/video_observations.md",
    "05_video_tests/avatar_a_mens_grooming/prompt_video_001.md",
    "05_video_tests/avatar_b_skincare_creator/video_observations.md",
    "05_video_tests/avatar_b_skincare_creator/prompt_video_001.md",
    "06_analysis/visual_defect_taxonomy.md",
    "06_analysis/observations.md",
    "07_report/report.md",
    "07_report/publish_checklist.md",
    "09_workflows/on1/avatar_a_realism_001_on1_photo_raw_2025.onp",
    "09_workflows/on1/on1_realism_001_settings_summary.md",
    "09_workflows/on1/avatar_b_realism_001_on1_photo_raw_2025.onp",
    "09_workflows/on1/on1_avatar_b_realism_001_settings_summary.md",
    "09_workflows/external_tool_notes.md",
    "scripts/build_html_report.py",
    "scripts/extract_face_crops.py",
    "scripts/lab_color_stats.py",
    "scripts/make_contact_sheet.py",
    "scripts/make_comparison_grid.py",
    "scripts/make_crop_comparison_grid.py",
    "scripts/prepare_video_test_package.py",
    "scripts/register_video_outputs.py",
    "scripts/register_dataset.py",
    "scripts/validate_project_structure.py",
]

CSV_HEADERS = {
    "02_source_data/dataset_register.csv": [
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
    ],
    "03_base_avatars/base_avatar_register.csv": [
        "avatar_id",
        "avatar_name",
        "niche",
        "tool_used",
        "prompt_file",
        "output_file",
        "selected",
        "reason",
        "notes",
    ],
    "04_realism_passes/realism_run_log.csv": [
        "run_id",
        "avatar_id",
        "input_file",
        "tool_used",
        "pass_type",
        "settings_summary",
        "output_file",
        "skin_realism",
        "eye_realism",
        "lips_realism",
        "hair_beard_realism",
        "identity_consistency",
        "overall_score",
        "verdict",
        "notes",
    ],
    "05_video_tests/video_test_log.csv": [
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
    ],
}


def read_csv_header(path: Path) -> list[str] | None:
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            return next(csv.reader(handle), None)
    except FileNotFoundError:
        return None


def main() -> int:
    missing_dirs = [item for item in REQUIRED_DIRS if not (ROOT / item).is_dir()]
    missing_files = [item for item in REQUIRED_FILES if not (ROOT / item).is_file()]

    invalid_csv = []
    for relative_path, expected_header in CSV_HEADERS.items():
        actual_header = read_csv_header(ROOT / relative_path)
        if actual_header != expected_header:
            invalid_csv.append((relative_path, actual_header, expected_header))

    if not missing_dirs and not missing_files and not invalid_csv:
        print("OK: project scaffold is valid.")
        print(f"Checked directories: {len(REQUIRED_DIRS)}")
        print(f"Checked files: {len(REQUIRED_FILES)}")
        print(f"Checked CSV files: {len(CSV_HEADERS)}")
        return 0

    print("INVALID: project scaffold has issues.")

    if missing_dirs:
        print("\nMissing directories:")
        for item in missing_dirs:
            print(f"- {item}")

    if missing_files:
        print("\nMissing files:")
        for item in missing_files:
            print(f"- {item}")

    if invalid_csv:
        print("\nInvalid CSV headers:")
        for relative_path, actual_header, expected_header in invalid_csv:
            print(f"- {relative_path}")
            print(f"  actual:   {actual_header}")
            print(f"  expected: {expected_header}")

    return 1


if __name__ == "__main__":
    sys.exit(main())

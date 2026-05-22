# Заметки по внешним инструментам

Здесь фиксируются внешние инструменты для generation, enhancement, video и upscale.

Записывать только те инструменты, которые реально тестировались или осознанно выбраны для проекта.

## ON1 Photo RAW 2025

Использован для `realism_001` Avatar A.

- Input: `03_base_avatars/avatar_a_mens_grooming/selected/base.jpg`
- Output: `04_realism_passes/avatar_a_mens_grooming/final_stills/final_realism_001.jpg`
- ON1 settings file: `09_workflows/on1/avatar_a_realism_001_on1_photo_raw_2025.onp`
- Readable summary: `09_workflows/on1/on1_realism_001_settings_summary.md`

Использован для `avatar_b_realism_001` Avatar B.

- Input: `03_base_avatars/avatar_b_skincare_creator/selected/base.jpg`
- Output: `04_realism_passes/avatar_b_skincare_creator/final_stills/final_realism_001.jpg`
- ON1 settings file: `09_workflows/on1/avatar_b_realism_001_on1_photo_raw_2025.onp`
- Readable summary: `09_workflows/on1/on1_avatar_b_realism_001_settings_summary.md`

## Magnific / Kling 3.0

Использован для image-to-video outputs.

- Site: `www.magnific.com`
- Model: `Kling 3.0`
- Avatar A input: `05_video_tests/avatar_a_mens_grooming/input_stills/avatar_a_realism_001_input.jpg`
- Avatar A output: `05_video_tests/avatar_a_mens_grooming/video_outputs/avatar_a_video_001.mp4`
- Avatar B input: `05_video_tests/avatar_b_skincare_creator/input_stills/avatar_b_realism_001_input.jpg`
- Avatar B output: `05_video_tests/avatar_b_skincare_creator/video_outputs/avatar_b_video_001.mp4`
- Scores are recorded in `05_video_tests/video_test_log.csv`.

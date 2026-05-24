# AI UGC Avatar Realism Pipeline for Beauty & Grooming Brands

## 1. Executive Summary

This case study documents a traceable workflow for improving and evaluating AI/UGC avatar realism for beauty, skincare, and men's grooming content.

The project includes:

- 2 avatar tracks: men's grooming and skincare creator.
- 2 ON1 Photo RAW 2025 realism passes.
- Face-zone crop comparison for skin, eyes, lips, and hair/beard or hairline.
- Manual realism scoring on a 1-5 scale.
- 2 image-to-video tests generated with Magnific / Kling 3.0.
- A published static HTML case study.

The goal is not to claim a production-ready avatar system. The goal is to show a structured, inspectable process for avatar realism evaluation.

## 2. Why This Case Matters

UGC-style AI avatars often look convincing in a full-frame still but fail in specific face zones or during motion. Before moving to image-to-video, the following areas need separate inspection:

- skin texture;
- eyes;
- lips;
- hair, beard, or hairline;
- identity consistency.

This project focuses on the workflow: source tracking, tool settings, crop comparison, manual scoring, video tests, and honest limitations.

## 3. Target Use Cases

### Avatar A: Men's Grooming Advisor

- Niche: men's grooming.
- Example use cases: face wash, beard care, moisturizer, shaving, fragrance, body care.

### Avatar B: Skincare Routine Creator

- Niche: skincare and beauty UGC.
- Example use cases: skincare routine, moisturizer, cleanser, serum, beauty education.

## 4. Method

The workflow used in this case:

1. Track public source references and license notes.
2. Select a base avatar still.
3. Create a realism pass with ON1 Photo RAW 2025.
4. Generate full-image comparison grids.
5. Extract face-zone crops.
6. Generate crop comparison grids.
7. Score realism manually on a 1-5 scale.
8. Prepare image-to-video prompts and input stills.
9. Generate short video tests with Magnific / Kling 3.0.
10. Score video stability manually on a 1-5 scale.

## 5. Source References and License Notes

### Avatar A

- File: `02_source_data/public_references/pexels_unsplash/mens_grooming_pexels_001.jpg`
- Source: Pexels
- Source URL: https://www.pexels.com/ru-ru/photo/11772165/
- License note: Pexels license checked on 2026-05-20.

### Avatar B

- File: `02_source_data/public_references/pexels_unsplash/skincare_creator_pexels_001.jpg`
- Source: Pexels
- Source URL: https://www.pexels.com/ru-ru/photo/4575002/
- License note: Pexels license checked on 2026-05-20.

Important limitation: the people in the reference images should not be presented as endorsing any product, brand, or service.

## 6. Avatar A: Men's Grooming Advisor

Character files:

- `01_character_briefs/avatar_a_mens_grooming/character_brief.md`
- `01_character_briefs/avatar_a_mens_grooming/character_profile.json`
- `01_character_briefs/avatar_a_mens_grooming/prompt_history.md`

Base avatar:

- `03_base_avatars/avatar_a_mens_grooming/selected/base.jpg`

Realism output:

- `04_realism_passes/avatar_a_mens_grooming/final_stills/final_realism_001.jpg`

Tooling:

- Tool: ON1 Photo RAW 2025
- Settings file: `09_workflows/on1/avatar_a_realism_001_on1_photo_raw_2025.onp`
- Readable settings summary: `09_workflows/on1/on1_realism_001_settings_summary.md`

## 7. Avatar B: Skincare Routine Creator

Character files:

- `01_character_briefs/avatar_b_skincare_creator/character_brief.md`
- `01_character_briefs/avatar_b_skincare_creator/character_profile.json`
- `01_character_briefs/avatar_b_skincare_creator/prompt_history.md`

Base avatar:

- `03_base_avatars/avatar_b_skincare_creator/selected/base.jpg`

Realism output:

- `04_realism_passes/avatar_b_skincare_creator/final_stills/final_realism_001.jpg`

Tooling:

- Tool: ON1 Photo RAW 2025
- Settings file: `09_workflows/on1/avatar_b_realism_001_on1_photo_raw_2025.onp`
- Readable settings summary: `09_workflows/on1/on1_avatar_b_realism_001_settings_summary.md`

## 8. Visual Comparison

Avatar A full-image comparison:

![Avatar A base vs realism](assets/images/avatar_a_mens_grooming_base_vs_realism_001.jpg)

Avatar A crop comparison:

![Avatar A crop comparison](assets/images/avatar_a_mens_grooming_crop_comparison_001.jpg)

Avatar B full-image comparison:

![Avatar B base vs realism](assets/images/avatar_b_skincare_creator_base_vs_realism_001.jpg)

Avatar B crop comparison:

![Avatar B crop comparison](assets/images/avatar_b_skincare_creator_crop_comparison_001.jpg)

Crop zones:

- `skin_forehead`
- `skin_cheeks`
- `eyes`
- `lips`
- `hair_beard`

For Avatar B, the `hair_beard` zone is used as a shared scoring column and represents hair/hairline.

## 9. Still-Image Realism Scoring

Scoring source: manual visual review after crop correction and crop comparison.

### Avatar A

| Metric | Score | Notes |
|---|---:|---|
| skin_realism | 4 | Skin is strong enough for a case-study draft. |
| eye_realism | 3 | Eyes are acceptable but remain a potential improvement area. |
| lips_realism | 4 | Lips are strong enough for a case-study draft. |
| hair_beard_realism | 3 | Beard is acceptable but can be improved in a second pass. |
| identity_consistency | 5 | Identity is preserved very well. |
| overall_score | 4 | Accepted for the case-study draft. |

Verdict: `accepted_for_case_draft`

### Avatar B

| Metric | Score | Notes |
|---|---:|---|
| skin_realism | 4 | Skin is strong enough for a case-study draft. |
| eye_realism | 5 | Eyes are the strongest area of this pass. |
| lips_realism | 4 | Lips are strong enough for a case-study draft. |
| hair_beard_realism | 4 | For this avatar, this represents hair/hairline. |
| identity_consistency | 4 | Identity is preserved well. |
| overall_score | 4 | Accepted for the case-study draft. |

Verdict: `accepted_for_case_draft`

CSV log:

- `04_realism_passes/realism_run_log.csv`

## 10. Color and Tone Statistics

Stats files:

- `06_analysis/lab_color_stats/avatar_a_mens_grooming_color_stats.csv`
- `06_analysis/lab_color_stats/avatar_b_skincare_creator_color_stats.csv`

Avatar A: `final_realism_001` became slightly darker across all crop zones, while saturation increased slightly in most zones.

| Zone | Luminance delta | Saturation delta | Chroma proxy delta |
|---|---:|---:|---:|
| eyes | -0.0245 | +0.0136 | +0.0018 |
| hair_beard | -0.0088 | +0.0049 | +0.0001 |
| lips | -0.0137 | +0.0067 | -0.0026 |
| skin_cheeks | -0.0224 | +0.0124 | +0.0018 |
| skin_forehead | -0.0342 | +0.0175 | +0.0042 |

Avatar B: `final_realism_001` became brighter and more saturated across all crop zones.

| Zone | Luminance delta | Saturation delta | Chroma proxy delta |
|---|---:|---:|---:|
| eyes | +0.0428 | +0.0421 | +0.0663 |
| hair_beard | +0.0315 | +0.0338 | +0.0513 |
| lips | +0.0284 | +0.0464 | +0.0644 |
| skin_cheeks | +0.0317 | +0.0479 | +0.0681 |
| skin_forehead | +0.0288 | +0.0493 | +0.0649 |

Limitation: these are RGB/HSV/luminance statistics, not a full LAB analysis. They help identify color and tone shifts but do not replace visual scoring.

## 11. Video Tests

Image-to-video tool:

- Platform: Magnific
- Model: Kling 3.0
- Website: `www.magnific.com`

Prepared inputs:

| Video run | Avatar | Input still | Prompt | Status |
|---|---|---|---|---|
| avatar_a_video_001 | avatar_a_mens_grooming | `05_video_tests/avatar_a_mens_grooming/input_stills/avatar_a_realism_001_input.jpg` | `05_video_tests/avatar_a_mens_grooming/prompt_video_001.md` | accepted_for_case_draft |
| avatar_b_video_001 | avatar_b_skincare_creator | `05_video_tests/avatar_b_skincare_creator/input_stills/avatar_b_realism_001_input.jpg` | `05_video_tests/avatar_b_skincare_creator/prompt_video_001.md` | accepted_for_case_draft |

Output videos:

![Avatar A video test](assets/video/avatar_a_video_001.mp4)

![Avatar B video test](assets/video/avatar_b_video_001.mp4)

Technical metadata:

| Video run | Output file | Duration | Resolution | Codec |
|---|---|---:|---|---|
| avatar_a_video_001 | `05_video_tests/avatar_a_mens_grooming/video_outputs/avatar_a_video_001.mp4` | 5.04 sec | 1176x1764 | H.264 |
| avatar_b_video_001 | `05_video_tests/avatar_b_skincare_creator/video_outputs/avatar_b_video_001.mp4` | 5.04 sec | 1080x1920 | H.264 |

Video scoring:

| Video run | face_stability | eye_stability | lips_stability | skin_stability | identity_consistency | overall_score | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| avatar_a_video_001 | 5 | 5 | 5 | 5 | 5 | 5 | accepted_for_case_draft |
| avatar_b_video_001 | 5 | 5 | 5 | 5 | 5 | 5 | accepted_for_case_draft |

## 12. What Worked

- Source images are tracked through `dataset_register.csv`.
- Pexels URLs and license notes are documented.
- ON1 settings are saved as workflow artifacts.
- Crop extraction made it possible to inspect specific face zones instead of relying only on full-frame impressions.
- Crop comparison grids made manual scoring easier and more transparent.
- Both video outputs were accepted for the case-study draft.

## 13. Limitations

- The scoring is manual and subjective.
- The color/tone analysis is simple RGB/HSV/luminance analysis, not a full LAB workflow.
- Avatar A eyes and beard scored lower than other areas, so they remain candidates for a second realism pass.
- The case should not be described as a commercial-ready avatar system.
- The source portraits are public references; they should not be used to imply endorsement by the people shown.

## 14. Current Status

This project is complete as a portfolio-grade case study.

Avatar A includes:

- source reference;
- base still;
- realism still;
- ON1 settings;
- full comparison;
- crop comparison;
- still-image scoring;
- video test;
- video scoring.

Avatar B includes:

- source reference;
- base still;
- realism still;
- ON1 settings;
- full comparison;
- crop comparison;
- color/tone statistics;
- still-image scoring;
- video test;
- video scoring.

## 15. Recommended Next Step

The next portfolio step should be a more commercial UGC case: a specific product, a tighter content script, and a short avatar-led product demonstration or routine.

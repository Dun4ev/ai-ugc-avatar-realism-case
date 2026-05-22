# Video Test Prompt: Avatar B

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

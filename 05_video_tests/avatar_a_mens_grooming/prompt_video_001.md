# Video Test Prompt: Avatar A

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

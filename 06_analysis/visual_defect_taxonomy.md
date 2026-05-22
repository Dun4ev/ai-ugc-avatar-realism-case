# Таксономия визуальных дефектов

| Defect | Описание | Возможная причина | Направление исправления |
|---|---|---|---|
| plastic_skin | Кожа выглядит восковой, слишком сглаженной или без тональных вариаций. | Слишком сильное smoothing или beauty strength. | Снизить силу обработки, добавить естественную вариативность, проверить crops. |
| glassy_eyes | Глаза выглядят мокрыми, стеклянными или искусственными. | Prompt, enhancer или video model слишком сильно меняют глаза. | Сохранять глаза, снизить eye transformation. |
| rubber_lips | Губы теряют текстуру или естественный контур. | Over-enhancement или плохая анимация. | Снизить mouth/lip manipulation. |
| beard_artifacts | Борода выглядит нарисованной или мерцает. | Слабый base avatar или нестабильность video model. | Улучшить still, уточнить crop, снизить motion. |
| identity_drift | Лицо меняется между passes. | Слишком сильная регенерация. | Снизить transformation strength и использовать selected stills. |
| overbeautified | Результат выглядит как generic AI influencer. | Prompt или style слишком generic. | Сделать character brief более конкретным. |
| ashy_skin | Темная или теплая кожа становится серой/washed out. | Неверная color correction или over-lighting. | Использовать tone-safe correction. |
| video_face_slip | Лицо съезжает или морфится в видео. | Слабый still или слишком сильный motion. | Улучшить still и снизить motion prompt. |

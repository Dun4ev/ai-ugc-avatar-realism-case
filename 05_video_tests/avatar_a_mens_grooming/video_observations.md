# Video Observations: Avatar A

## 2026-05-21: Подготовка video test 001

### Факты

- Input still подготовлен: `05_video_tests/avatar_a_mens_grooming/input_stills/avatar_a_realism_001_input.jpg`.
- Prompt подготовлен: `05_video_tests/avatar_a_mens_grooming/prompt_video_001.md`.
- CSV row добавлена в `05_video_tests/video_test_log.csv` как `avatar_a_video_001`.
- Статус: `pending_generation`.

### Ограничение

Видео еще не сгенерировано. Оценки face/eyes/lips/skin/identity не выставлены.

### Следующий шаг

Сгенерировать короткий image-to-video test во внешнем инструменте и положить результат в `05_video_tests/avatar_a_mens_grooming/video_outputs/`.

## 2026-05-21: Video output received

### Факты

- Output video добавлен: `05_video_tests/avatar_a_mens_grooming/video_outputs/avatar_a_video_001.mp4`.
- Codec: H.264.
- Resolution: 1176x1764.
- Duration: 5.04 sec.
- Копия для отчета: `07_report/assets/video/avatar_a_video_001.mp4`.
- CSV row обновлена в `05_video_tests/video_test_log.csv`.
- Статус: `pending_review`.

### Ограничение

Инструмент генерации указан пользователем: Magnific, модель Kling 3.0, `www.magnific.com`.

## 2026-05-22: Video scoring

### Оценки пользователя

| Metric | Score |
|---|---:|
| face_stability | 5 |
| eye_stability | 5 |
| lips_stability | 5 |
| skin_stability | 5 |
| identity_consistency | 5 |
| overall_score | 5 |

### Итог

`avatar_a_video_001` принят как `accepted_for_case_draft`.

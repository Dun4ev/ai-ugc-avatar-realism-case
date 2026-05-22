# Наблюдения

Визуальные эксперименты пока не проводились.

Использовать этот файл, чтобы разделять:

- факты из source files;
- визуальные наблюдения;
- предполагаемые причины;
- открытые вопросы;
- следующие действия.

## 2026-05-20: Avatar A initial portrait

### Факты

- Добавлен первый men's grooming portrait reference: `02_source_data/public_references/pexels_unsplash/mens_grooming_pexels_001.jpg`.
- Добавлен base avatar файл: `03_base_avatars/avatar_a_mens_grooming/selected/base.jpg`.
- Добавлен current final placeholder: `04_realism_passes/avatar_a_mens_grooming/final_stills/final.jpg`.
- Создан comparison grid: `06_analysis/comparison_grids/avatar_a_mens_grooming_comparison_001.jpg`.

### Ограничение

`base.jpg` и `final.jpg` сейчас являются одним и тем же изображением под разными именами. Это можно использовать для проверки структуры и скриптов, но нельзя считать доказательством realism pass.

### Следующий шаг

Нужен реальный altered/improved still для Avatar A, чтобы сравнение стало содержательным.

## 2026-05-20: Avatar A realism pass 001

### Факты

- Добавлен improved still: `04_realism_passes/avatar_a_mens_grooming/final_stills/final_realism_001.jpg`.
- Размер изображения совпадает с base: 4000x6000 RGB.
- Создана comparison grid: `06_analysis/comparison_grids/avatar_a_mens_grooming_base_vs_realism_001.jpg`.
- Копия для отчета: `07_report/assets/images/avatar_a_mens_grooming_base_vs_realism_001.jpg`.
- Прогон добавлен в `04_realism_passes/realism_run_log.csv` как `realism_001`.

### Ограничение

Точный инструмент и настройки enhancement пока не записаны. Оценки skin/eyes/lips/beard/identity не выставлены, чтобы не подменять визуальный review автоматическим предположением.

### Следующий шаг

Провести visual scoring `realism_001` по шкале 1-5 и обновить `realism_run_log.csv`.

## 2026-05-20: Avatar A crop extraction

### Факты

- Реализован `scripts/extract_face_crops.py`.
- Для `base.jpg` и `final_realism_001.jpg` извлечено 10 crop-файлов.
- Зоны: `skin_forehead`, `skin_cheeks`, `eyes`, `lips`, `hair_beard`.
- Manifest сохранен в `06_analysis/crops/avatar_a_mens_grooming/crop_manifest.csv`.

### Ограничение

Текущие crop-зоны построены по пропорциональным координатам для centered portrait. Это достаточно для первого review, но при необходимости зоны можно уточнить вручную через параметры `--zone`.

### Следующий шаг

Оценить `realism_001` по crop-файлам и comparison grid, затем заполнить score-поля в `04_realism_passes/realism_run_log.csv`.

### Уточнение после проверки

Первая версия координат была неточной для этого кадра: зоны попадали выше нужных областей лица. Координаты в `scripts/extract_face_crops.py` обновлены под текущий close-up portrait, crops перегенерированы с `--overwrite`.

Текущие зоны:

- `eyes`: оба глаза и область вокруг глаз.
- `lips`: губы и прилегающая зона усов/бороды.
- `hair_beard`: усы, губы, борода и нижняя часть лица.
- `skin_forehead`: лоб.
- `skin_cheeks`: щеки и центральная кожа лица без зоны лба.

## 2026-05-20: Avatar A crop comparison grid

### Факты

- Реализован `scripts/make_crop_comparison_grid.py`.
- Создана grid-таблица `base` vs `final_realism_001` по зонам:
  - `skin_forehead`
  - `skin_cheeks`
  - `eyes`
  - `lips`
  - `hair_beard`
- Analysis copy: `06_analysis/comparison_grids/avatar_a_mens_grooming_crop_comparison_001.jpg`.
- Report asset copy: `07_report/assets/images/avatar_a_mens_grooming_crop_comparison_001.jpg`.

### Следующий шаг

Использовать crop comparison grid как основной артефакт для scoring `realism_001`.

## 2026-05-20: Avatar A color/tone stats

### Факты

- Реализован `scripts/lab_color_stats.py`.
- Посчитана таблица: `06_analysis/lab_color_stats/avatar_a_mens_grooming_color_stats.csv`.
- Проанализировано 10 crop-файлов.

### Наблюдения

По сравнению с `base`, `final_realism_001` стал немного темнее во всех crop-зонах:

| Zone | Luminance delta | Saturation delta | Chroma proxy delta |
|---|---:|---:|---:|
| eyes | -0.0245 | +0.0136 | +0.0018 |
| hair_beard | -0.0088 | +0.0049 | +0.0001 |
| lips | -0.0137 | +0.0067 | -0.0026 |
| skin_cheeks | -0.0224 | +0.0124 | +0.0018 |
| skin_forehead | -0.0342 | +0.0175 | +0.0042 |

### Ограничение

Это простые RGB/HSV/luminance statistics, а не полноценный LAB analysis. Они помогают увидеть tonal/color shift, но не заменяют визуальный scoring.

## 2026-05-20: Avatar B initial portrait

### Факты

- Добавлен skincare/beauty close-up portrait reference: `02_source_data/public_references/pexels_unsplash/skincare_creator_pexels_001.jpg`.
- Source URL: https://www.pexels.com/ru-ru/photo/4575002/
- Добавлен base avatar файл: `03_base_avatars/avatar_b_skincare_creator/selected/base.jpg`.
- Созданы character files:
  - `01_character_briefs/avatar_b_skincare_creator/character_brief.md`
  - `01_character_briefs/avatar_b_skincare_creator/character_profile.json`
  - `01_character_briefs/avatar_b_skincare_creator/prompt_history.md`
- Base avatar добавлен в `03_base_avatars/base_avatar_register.csv`.

### Ограничение

Realism pass для Avatar B пока не выполнен. Сейчас это только source/base этап.

### Следующий шаг

Подготовить `final_realism_001.jpg` для Avatar B через ON1 Photo RAW 2025 или другой enhancement tool, затем повторить comparison/crops/scoring workflow.

## 2026-05-21: Avatar B realism pass 001

### Факты

- Добавлен improved still: `04_realism_passes/avatar_b_skincare_creator/final_stills/final_realism_001.jpg`.
- Размер изображения совпадает с base: 2587x4599 RGB.
- Инструмент: ON1 Photo RAW 2025.
- Настройки сохранены в `09_workflows/on1/avatar_b_realism_001_on1_photo_raw_2025.onp`.
- Читаемый summary: `09_workflows/on1/on1_avatar_b_realism_001_settings_summary.md`.
- Прогон добавлен в `04_realism_passes/realism_run_log.csv` как `avatar_b_realism_001`.
- Создана full comparison grid: `06_analysis/comparison_grids/avatar_b_skincare_creator_base_vs_realism_001.jpg`.

### Наблюдение

Визуально pass делает изображение светлее, теплее и насыщеннее. Для skincare-кейса это может выглядеть более polished, но scoring нужно делать осторожно: слишком сильное сглаживание/осветление может ухудшить skin realism.

### Ограничение

Оценки заполнены после user visual scoring по crop comparison. `avatar_b_realism_001` принят для черновика кейса.

## 2026-05-21: Avatar B crop comparison

### Факты

- Для `base.jpg` и `final_realism_001.jpg` извлечено 10 crop-файлов.
- Manifest: `06_analysis/crops/avatar_b_skincare_creator/crop_manifest.csv`.
- Crop comparison grid: `06_analysis/comparison_grids/avatar_b_skincare_creator_crop_comparison_001.jpg`.
- Зоны:
  - `skin_forehead`
  - `skin_cheeks`
  - `eyes`
  - `lips`
  - `hair_beard`

### Уточнение

Для Avatar B зона `hair_beard` фактически используется как `hair/hairline`, чтобы сохранить единую scoring-колонку CSV между Avatar A и Avatar B.

## 2026-05-21: Avatar B color/tone stats

### Факты

- Посчитана таблица: `06_analysis/lab_color_stats/avatar_b_skincare_creator_color_stats.csv`.
- Проанализировано 10 crop-файлов.

### Наблюдения

По сравнению с `base`, `final_realism_001` стал светлее и насыщеннее во всех crop-зонах:

| Zone | Luminance delta | Saturation delta | Chroma proxy delta |
|---|---:|---:|---:|
| eyes | +0.0428 | +0.0421 | +0.0663 |
| hair_beard | +0.0315 | +0.0338 | +0.0513 |
| lips | +0.0284 | +0.0464 | +0.0644 |
| skin_cheeks | +0.0317 | +0.0479 | +0.0681 |
| skin_forehead | +0.0288 | +0.0493 | +0.0649 |

### Ограничение

Это простые RGB/HSV/luminance statistics, а не полноценный LAB analysis. Они показывают tonal/color shift, но не заменяют visual scoring.

## 2026-05-21: Avatar B realism scoring

### Оценки пользователя

| Metric | Score | Комментарий |
|---|---:|---|
| skin_realism | 4 | Кожа оценена как хорошая для case draft. |
| eye_realism | 5 | Глаза — самая сильная зона текущего pass. |
| lips_realism | 4 | Губы оценены как хорошие для case draft. |
| hair_beard_realism | 4 | Для Avatar B это hair/hairline зона; результат оценен как хороший. |
| identity_consistency | 4 | Личность сохранена хорошо. |
| overall_score | 4 | Realism pass можно использовать в черновике кейса. |

### Итог

`avatar_b_realism_001` принят как `accepted_for_case_draft`. Главная сильная зона — eyes. Ограничение: identity consistency хорошая, но не максимальная.

## 2026-05-21: Video test preparation

### Факты

- Реализован `scripts/prepare_video_test_package.py`.
- Подготовлены input stills:
  - `05_video_tests/avatar_a_mens_grooming/input_stills/avatar_a_realism_001_input.jpg`
  - `05_video_tests/avatar_b_skincare_creator/input_stills/avatar_b_realism_001_input.jpg`
- Подготовлены prompt files:
  - `05_video_tests/avatar_a_mens_grooming/prompt_video_001.md`
  - `05_video_tests/avatar_b_skincare_creator/prompt_video_001.md`
- В `05_video_tests/video_test_log.csv` добавлены pending-записи:
  - `avatar_a_video_001`
  - `avatar_b_video_001`

### Ограничение

Видео не генерировалось. В CSV нет output video, duration и stability scores, потому что это будет отдельный этап после внешней генерации.

## 2026-05-21: Video outputs registered

### Факты

- Зарегистрированы video outputs:
  - `05_video_tests/avatar_a_mens_grooming/video_outputs/avatar_a_video_001.mp4`
  - `05_video_tests/avatar_b_skincare_creator/video_outputs/avatar_b_video_001.mp4`
- Длительность обоих видео: 5.04 sec.
- Avatar A video: H.264, 1176x1764.
- Avatar B video: H.264, 1080x1920.
- Видео скопированы в `07_report/assets/video/` для HTML-отчета.
- Реализован `scripts/register_video_outputs.py`.

### Ограничение

Инструмент генерации уточнен пользователем позже: Magnific, модель Kling 3.0, `www.magnific.com`.

## 2026-05-22: Video scoring

### Оценки пользователя

| Video run | face_stability | eye_stability | lips_stability | skin_stability | identity_consistency | overall_score | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| avatar_a_video_001 | 5 | 5 | 5 | 5 | 5 | 5 | accepted_for_case_draft |
| avatar_b_video_001 | 5 | 5 | 5 | 5 | 5 | 5 | accepted_for_case_draft |

### Ограничение

Инструмент генерации video outputs: Magnific, модель Kling 3.0, `www.magnific.com`.

## 2026-05-20: Avatar A realism scoring

### Оценки пользователя

| Metric | Score | Комментарий |
|---|---:|---|
| skin_realism | 4 | Кожа оценена как хорошая для case draft. |
| eye_realism | 3 | Глаза приемлемы для эксперимента, но без сильного улучшения. |
| lips_realism | 4 | Губы оценены как хорошие для case draft. |
| hair_beard_realism | 3 | Волосы/борода приемлемы, но не strongest area. |
| identity_consistency | 5 | Личность сохранена очень хорошо. |
| overall_score | 4 | Realism pass можно использовать в черновике кейса. |

### Итог

`realism_001` принят как `accepted_for_case_draft`. Основные ограничения: eyes и hair/beard остаются зонами для дальнейшего улучшения.

### Инструмент

Пользователь уточнил, что `realism_001` сделан в ON1 Photo RAW 2025. Настройки сохранены в `09_workflows/on1/avatar_a_realism_001_on1_photo_raw_2025.onp`, читаемый summary — в `09_workflows/on1/on1_realism_001_settings_summary.md`.

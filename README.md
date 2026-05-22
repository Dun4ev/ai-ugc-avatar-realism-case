# AI UGC Avatar Realism Case

Личный case study для проектирования и документирования pipeline повышения реалистичности AI-аватаров в beauty, skincare и men's grooming UGC-сценариях.

Проект фокусируется на том, как сделать AI-generated avatar stills более пригодными для коротких UGC-style video tests через диагностику и улучшение реалистичности кожи, глаз, губ, волос и бороды до image-to-video генерации.

## Цели

- Создать два направления кейса: men's grooming и skincare routine creator.
- Документировать character briefs, base avatar candidates, realism passes и visual defects.
- Отслеживать важные эксперименты через CSV-логи.
- Подготовить финальный Markdown и HTML-отчет для публикации как static case study.
- Явно показывать limitations, failed experiments и права на источники.

## Ожидаемые результаты

- Структурированный проектный репозиторий.
- Character profiles в Markdown и JSON.
- Base и improved avatar stills.
- Crop-сравнения ключевых зон лица.
- Короткие image-to-video tests.
- Experiment logs в CSV.
- Финальный `07_report/report.html`.
- Publication-ready `08_site/index.html`.

## Локальная настройка

Создавать виртуальное окружение и ставить зависимости нужно только когда они реально понадобятся для скриптов:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Проверить текущий scaffold:

```bash
python3 scripts/validate_project_structure.py
```

Зарегистрировать исходные изображения после добавления файлов в `02_source_data/`:

```bash
python3 scripts/register_dataset.py
```

Создать contact sheet по зарегистрированным изображениям:

```bash
python3 scripts/make_contact_sheet.py
```

В contact sheet попадают строки, где `allowed_for_public_report` равно `yes` или заполнено поле `use_case`.

Создать comparison grid для base / realism / final изображений:

```bash
python3 scripts/make_comparison_grid.py \
  --avatar-id avatar_a_mens_grooming \
  --images path/to/base.jpg path/to/realism.jpg path/to/final.jpg \
  --labels "Base avatar" "Realism pass" "Final still"
```

Результат сохраняется в `06_analysis/comparison_grids/` и копируется в `07_report/assets/images/`. Существующий файл не перезаписывается без `--overwrite`.

Извлечь crop-зоны лица для анализа realism:

```bash
python3 scripts/extract_face_crops.py \
  --avatar-id avatar_a_mens_grooming \
  --images \
    03_base_avatars/avatar_a_mens_grooming/selected/base.jpg \
    04_realism_passes/avatar_a_mens_grooming/final_stills/final_realism_001.jpg
```

Результат сохраняется в `06_analysis/crops/<avatar_id>/` вместе с `crop_manifest.csv`.

Создать crop comparison grid для оценки realism по зонам:

```bash
python3 scripts/make_crop_comparison_grid.py \
  --avatar-id avatar_a_mens_grooming \
  --overwrite
```

Результат сохраняется в `06_analysis/comparison_grids/` и копируется в `07_report/assets/images/`.

ON1 Photo RAW 2025 settings для `realism_001`:

- preset: `09_workflows/on1/avatar_a_realism_001_on1_photo_raw_2025.onp`
- readable summary: `09_workflows/on1/on1_realism_001_settings_summary.md`

Посчитать color/tone statistics по crop-файлам:

```bash
python3 scripts/lab_color_stats.py \
  --avatar-id avatar_a_mens_grooming
```

Результат сохраняется в `06_analysis/lab_color_stats/`.

Собрать HTML-отчет и локальный static site:

```bash
python3 scripts/build_html_report.py
```

Результаты:

- `07_report/report.html`
- `08_site/index.html`

## Правила проекта

- Не перезаписывать исходные изображения.
- Хранить source materials в `02_source_data/`.
- Хранить generated outputs отдельно от исходников.
- Не коммитить private images, API keys, model files или heavy raw media.
- Не выдумывать результаты в отчетах. Ссылаться только на существующие файлы.

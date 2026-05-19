# PROJECT_BRIEF.md

# AI UGC Avatar Realism Case for Beauty & Grooming Brands

## 0. Назначение этого файла

Этот файл является стартовым техническим заданием для личного проекта.

Его нужно использовать как:

1. вводный документ для владельца проекта;
2. контекст для Codex;
3. основу для создания структуры репозитория;
4. основу для будущего `README.md`;
5. основу для публикации кейса на сайте.

Проект не является коммерческим заказом. Цель проекта: разобраться в создании реалистичных AI-аватаров и визуального UGC-контента для ниш Beauty, Skincare и Men's Grooming, а также подготовить портфолио-кейс, который можно опубликовать на личном сайте или GitHub Pages.

---

## 1. Краткое описание проекта

Название проекта:

**AI UGC Avatar Realism Pipeline for Beauty & Grooming Brands**

Суть проекта:

Создать небольшой исследовательский и визуальный кейс, который показывает, как базовый AI-аватар можно довести до более реалистичного и коммерчески пригодного состояния для UGC-контента в нишах:

- beauty;
- skincare;
- sensorial skincare;
- men's grooming;
- fragrance / body care;
- beauty devices.

Ключевой фокус:

- кожа не должна выглядеть пластиковой;
- глаза не должны выглядеть стеклянными;
- губы не должны выглядеть резиновыми;
- лицо должно сохранять реализм при подготовке к image-to-video;
- итоговый аватар должен быть пригоден для UGC-style рекламного или демонстрационного видео.

Проект должен показать не просто красивые картинки, а управляемый процесс:

1. постановка визуальной задачи;
2. создание character brief;
3. генерация базового аватара;
4. диагностика визуальных дефектов;
5. улучшение skin / eyes / lips / hair / beard realism;
6. короткий image-to-video тест;
7. документирование результата;
8. публикация в формате HTML-кейса.

---

## 2. Цель проекта

Главная цель:

> Создать личный портфолио-кейс, демонстрирующий способность проектировать и документировать AI visual tuning pipeline для реалистичных UGC-аватаров в нишах Beauty, Skincare и Men's Grooming.

Практические цели:

1. Разобраться в workflow генерации и улучшения AI-аватаров.
2. Научиться диагностировать визуальные дефекты AI-лиц.
3. Проверить, какие этапы нужны до image-to-video анимации.
4. Собрать доказательный HTML-кейс.
5. Подготовить проект так, чтобы его можно было развивать дальше в сторону портфолио, фриланса или MVP.

---

## 3. Критерий хорошего результата

Проект считается успешным, если в конце есть:

1. структурированный репозиторий;
2. минимум 2 AI-аватара:
   - men's grooming avatar;
   - skincare / beauty avatar;
3. character brief в JSON/Markdown для каждого аватара;
4. базовое изображение аватара;
5. улучшенное изображение аватара после realism pass;
6. crop-сравнения зон лица:
   - кожа;
   - глаза;
   - губы;
   - волосы / борода;
7. минимум 1 короткий image-to-video тест;
8. таблица экспериментов `run_log.csv`;
9. описание наблюдений и failure modes;
10. финальный HTML-отчет;
11. подготовленная версия для публикации на сайте.

---

## 4. Ограничения проекта

### 4.1. Железо

Основная машина:

- MacBook Air M4;
- 32 GB unified memory;
- macOS;
- без NVIDIA GPU.

Вывод:

- MacBook использовать как control center проекта;
- локально делать структуру, скрипты, анализ, отчеты, легкие ComfyUI-тесты;
- тяжелую генерацию, image-to-video и upscaling при необходимости выполнять через cloud GPU или веб-сервисы.

### 4.2. Бюджет

Допустимый бюджет на начальную фазу:

- локальная работа: бесплатно;
- cloud / paid tools: ориентир $20-30 для тестов.

Не покупать дорогие подписки до проверки гипотезы.

### 4.3. Масштаб

Не пытаться сразу строить полноценный SaaS или production pipeline.

На первом этапе проект должен быть case study, а не продукт.

---

## 5. Основная гипотеза

Гипотеза:

> Для коммерчески пригодного AI UGC-аватара важно не только сгенерировать красивое лицо, но и перед анимацией отдельно улучшить кожу, глаза, губы, волосы/бороду и общий уровень реализма. Если отправить слабый AI-still сразу в image-to-video, видео часто усиливает дефекты: пластиковую кожу, стеклянные глаза, плавающую мимику и deepfake-ощущение.

Что нужно проверить:

1. Улучшается ли восприятие аватара после отдельного realism pass.
2. Какие зоны лица чаще всего ломают реализм.
3. Помогают ли crop-анализ и таблица дефектов управляемо улучшать результат.
4. Насколько сложно получить короткое UGC-style видео без сильного uncanny valley эффекта.

---

## 6. Целевая ниша

Основные ниши:

1. Men's grooming
   - face wash;
   - shaving;
   - beard oil;
   - moisturizer;
   - hair styling;
   - fragrance.

2. Sensorial skincare
   - кремы;
   - сыворотки;
   - текстуры;
   - glow;
   - slow routine;
   - clean bathroom aesthetic;
   - premium упаковка.

3. Clean beauty
   - натуральность;
   - доверие;
   - состав;
   - простая рутина;
   - мягкая эстетика без медицинских обещаний.

Первый кейс должен сфокусироваться на двух персонажах:

1. **Avatar A: Men's Grooming Advisor**
2. **Avatar B: Skincare Routine Creator**

---

## 7. Что НЕ входит в первый этап

Не входит:

- создание SaaS;
- backend;
- billing;
- авторизация пользователей;
- обучение собственной LoRA;
- полноценное 3D-моделирование;
- сложный lip-sync production;
- массовая генерация сотен видео;
- коммерческий запуск;
- работа с клиентом;
- обещания эффективности рекламы;
- медицинские claims по skincare.

---

## 8. Рекомендуемая структура проекта

Codex должен создать следующую структуру:

```text
beauty-avatar-realism-case/
  PROJECT_BRIEF.md
  AGENTS.md
  README.md
  requirements.txt
  .gitignore

  00_project_control/
    project_goal.md
    decisions.md
    open_questions.md
    roadmap.md
    references.md

  01_character_briefs/
    avatar_a_mens_grooming/
      character_brief.md
      character_profile.json
      prompt_history.md
    avatar_b_skincare_creator/
      character_brief.md
      character_profile.json
      prompt_history.md

  02_source_data/
    public_references/
      pexels_unsplash/
      ppr10k_subset/
    generated_references/
    own_test_images/
    dataset_register.csv
    source_license_notes.md

  03_base_avatars/
    avatar_a_mens_grooming/
      candidates/
      selected/
    avatar_b_skincare_creator/
      candidates/
      selected/
    base_avatar_register.csv

  04_realism_passes/
    avatar_a_mens_grooming/
      pass_01_skin/
      pass_02_eyes/
      pass_03_lips/
      pass_04_hair_beard/
      final_stills/
    avatar_b_skincare_creator/
      pass_01_skin/
      pass_02_eyes/
      pass_03_lips/
      pass_04_hair/
      final_stills/
    realism_run_log.csv

  05_video_tests/
    avatar_a_mens_grooming/
      input_stills/
      video_outputs/
      video_observations.md
    avatar_b_skincare_creator/
      input_stills/
      video_outputs/
      video_observations.md
    video_test_log.csv

  06_analysis/
    crops/
    comparison_grids/
    contact_sheets/
    lab_color_stats/
    visual_defect_taxonomy.md
    observations.md

  07_report/
    report.md
    report.html
    assets/
      images/
      video/
      css/
    publish_checklist.md

  08_site/
    index.html
    assets/
    README_site.md

  09_workflows/
    comfyui/
      baseline_workflow.json
      realism_pass_workflow.json
    external_tool_notes.md

  scripts/
    register_dataset.py
    make_contact_sheet.py
    make_comparison_grid.py
    extract_face_crops.py
    lab_color_stats.py
    build_html_report.py
    validate_project_structure.py
```

---

## 9. Правила работы с файлами

1. Не изменять исходные изображения.
2. Все исходники хранить только в `02_source_data/`.
3. Все сгенерированные результаты хранить отдельно от исходников.
4. Все важные прогоны фиксировать в CSV.
5. Не коммитить тяжелые модели, кеши, временные файлы и приватные ключи.
6. Не публиковать private/personally sensitive изображения.
7. Для публичного кейса использовать только разрешенные изображения и/или собственные сгенерированные ассеты.
8. В отчете честно указывать limitations.

---

## 10. Рекомендуемый `.gitignore`

Codex должен создать `.gitignore` примерно такого вида:

```gitignore
# macOS
.DS_Store

# Python
__pycache__/
*.pyc
.venv/
venv/
.env

# Large model files
*.safetensors
*.ckpt
*.pt
*.pth
*.gguf
*.onnx
models/

# Generated heavy media
*.mov
*.mp4
*.avi
*.mkv
*.webm

# Temporary files
tmp/
.cache/

# ComfyUI outputs if copied accidentally
ComfyUI/output/
ComfyUI/input/
ComfyUI/temp/

# Private API keys
.env
secrets.*
```

Важно: для публикации можно хранить оптимизированные изображения и короткие видео в `07_report/assets/` или `08_site/assets/`, но тяжелые raw files лучше не коммитить.

---

## 11. Что установить локально

### 11.1. Базовые инструменты macOS

Установить:

1. Xcode Command Line Tools
2. Homebrew
3. Git
4. Python 3.11
5. Node.js LTS
6. VS Code или другой редактор
7. Codex CLI
8. ComfyUI Desktop или manual ComfyUI

Пояснение:

- Homebrew нужен для установки пакетов;
- Git нужен для версионирования;
- Python нужен для анализа, генерации таблиц и HTML-отчета;
- Node.js нужен для возможного сайта, статической сборки или tooling;
- Codex CLI нужен для разработки структуры и скриптов;
- ComfyUI нужен для визуальных экспериментов.

### 11.2. Пример команд установки

```bash
# 1. Xcode Command Line Tools
xcode-select --install

# 2. Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 3. Базовые пакеты
brew install git python@3.11 node ffmpeg imagemagick exiftool

# 4. Codex CLI, вариант через Homebrew
brew install --cask codex

# 5. Проверка
python3 --version
git --version
node --version
codex --version
ffmpeg -version
magick -version
```

Если `codex` не устанавливается через Homebrew, использовать вариант через npm:

```bash
npm install -g @openai/codex
```

---

## 12. Python-зависимости

Codex должен создать `requirements.txt`:

```txt
pandas
numpy
pillow
opencv-python
scikit-image
jinja2
markdown
openpyxl
python-dotenv
rich
```

Назначение:

- `pandas`: CSV/XLSX-таблицы;
- `numpy`: числовая обработка;
- `pillow`: работа с изображениями;
- `opencv-python`: crop, resize, basic image operations;
- `scikit-image`: LAB/HSV/statistics;
- `jinja2`: HTML-шаблоны;
- `markdown`: конвертация Markdown в HTML;
- `openpyxl`: экспорт XLSX;
- `python-dotenv`: локальные настройки;
- `rich`: красивый CLI-вывод.

Установка:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 13. ComfyUI

### 13.1. Рекомендуемый путь

На MacBook Air M4 начать с ComfyUI Desktop для Apple Silicon или с manual installation, если Desktop будет нестабилен.

Что сделать:

1. Установить ComfyUI Desktop для macOS Apple Silicon.
2. Проверить запуск.
3. Создать простой image-to-image workflow.
4. Сохранить workflow JSON в `09_workflows/comfyui/`.
5. Не смешивать рабочую папку ComfyUI с репозиторием кейса.

### 13.2. Что не делать на старте

Не начинать с тяжелого full Flux/Z-Image production workflow.

Сначала нужно получить управляемый baseline:

- input image;
- resize;
- image-to-image / enhancement;
- optional face/detail pass;
- output.

Затем можно постепенно добавлять:

- LoRA;
- ControlNet / tile;
- upscale;
- skin/detail enhancer;
- image-to-video service.

---

## 14. Внешние инструменты и сервисы

Проект должен быть tool-agnostic. Не привязываться к одному сервису.

Возможные категории:

### 14.1. Генерация аватара

Варианты:

- Higgsfield;
- Midjourney;
- Freepik / Magnific ecosystem;
- Ideogram;
- Leonardo;
- ComfyUI local/cloud workflow.

### 14.2. Улучшение реализма

Варианты:

- ComfyUI enhancer workflow;
- Magnific AI;
- Enhancor;
- Photoshop / Affinity Photo / Krita;
- Topaz Photo AI;
- локальные upscale/detail nodes.

### 14.3. Image-to-video

Варианты:

- Kling;
- Veo;
- Runway;
- Pika;
- Higgsfield;
- Luma;
- другие доступные сервисы.

### 14.4. Upscale видео

Варианты:

- Topaz Video;
- сервисный upscale;
- ComfyUI upscaler;
- ffmpeg для кодирования, но не для AI-upscale.

Важно: платные сервисы использовать только для небольшого количества финальных тестов.

---

## 15. Источники изображений

### 15.1. Основные источники

Использовать смешанный набор:

1. Pexels / Unsplash
   - реальные публичные портреты;
   - удобно для визуального кейса;
   - проверять лицензию и не делать misleading claims.

2. PPR10K subset
   - датасет portrait retouching;
   - использовать маленький subset для учебного анализа;
   - не публиковать массивно без проверки условий.

3. Сгенерированные изображения
   - использовать как stress tests;
   - не использовать как единственную основу кейса.

4. Собственные фото
   - использовать только при желании;
   - не публиковать без осознанного решения.

### 15.2. Минимальный dataset для первого этапа

```text
public_references:
  10 male grooming portraits
  10 skincare / beauty portraits
  5 dark skin / warm skin tone portraits
  5 close-up face references

generated_references:
  3 men's grooming avatar candidates
  3 skincare creator avatar candidates

ppr10k_subset:
  5-10 portrait retouching examples
```

Не нужно собирать 500 изображений. Для первого кейса достаточно 30-50 carefully selected images.

---

## 16. CSV-схемы

### 16.1. `dataset_register.csv`

```csv
image_id,source,license_note,filename,relative_path,subject_type,skin_tone,lighting,crop_type,use_case,allowed_for_public_report,notes
```

Примеры значений:

- `source`: pexels, unsplash, ppr10k, generated, own
- `subject_type`: male, female, product, face_closeup, hands, routine
- `skin_tone`: light, medium, olive, dark, unknown
- `lighting`: soft, harsh, low_light, studio, bathroom, outdoor
- `crop_type`: closeup, half_body, full_body, product_macro
- `use_case`: avatar_reference, skin_texture_test, eye_test, lips_test, video_test
- `allowed_for_public_report`: yes/no

### 16.2. `base_avatar_register.csv`

```csv
avatar_id,avatar_name,niche,tool_used,prompt_file,output_file,selected,reason,notes
```

### 16.3. `realism_run_log.csv`

```csv
run_id,avatar_id,input_file,tool_used,pass_type,settings_summary,output_file,skin_realism,eye_realism,lips_realism,hair_beard_realism,identity_consistency,overall_score,verdict,notes
```

Оценки по шкале 1-5.

### 16.4. `video_test_log.csv`

```csv
video_run_id,avatar_id,input_still,tool_used,prompt_file,output_video,duration_sec,face_stability,eye_stability,lips_stability,skin_stability,identity_consistency,overall_score,verdict,notes
```

---

## 17. Character profile JSON

Для каждого аватара создать `character_profile.json`.

Пример для men's grooming:

```json
{
  "avatar_id": "avatar_a_mens_grooming",
  "character_name": "Milan",
  "niche": "men's grooming",
  "age_range": "32-38",
  "skin_tone": "medium olive",
  "face_shape": "oval",
  "hair": "short dark blond or light brown hair, clean haircut",
  "facial_hair": "short well-groomed beard",
  "brand_role": "premium but approachable grooming advisor",
  "visual_style": "clean bathroom, soft premium light, practical masculine skincare routine",
  "personality": "calm, competent, minimal, trustworthy",
  "visual_risks": [
    "plastic skin",
    "fake beard texture",
    "glassy eyes",
    "over-polished face",
    "AI influencer look"
  ],
  "success_criteria": [
    "natural skin finish",
    "realistic eyes",
    "stable beard texture",
    "premium grooming aesthetic",
    "ready for short UGC video test"
  ]
}
```

Пример для skincare:

```json
{
  "avatar_id": "avatar_b_skincare_creator",
  "character_name": "Sofia",
  "niche": "sensorial skincare",
  "age_range": "28-35",
  "skin_tone": "warm medium",
  "face_shape": "soft oval",
  "hair": "soft natural hair, clean styling",
  "brand_role": "skincare routine creator",
  "visual_style": "warm bathroom light, clean beauty, serum texture, calm morning routine",
  "personality": "gentle, precise, confident, sensory",
  "visual_risks": [
    "waxy skin",
    "over-glowing face",
    "glassy eyes",
    "rubber lips",
    "too perfect influencer face"
  ],
  "success_criteria": [
    "soft but realistic skin",
    "visible natural tonal variation",
    "non-glassy eyes",
    "natural lips",
    "ready for skincare UGC video test"
  ]
}
```

---

## 18. Визуальная таксономия дефектов

Codex должен создать `06_analysis/visual_defect_taxonomy.md`.

Базовые категории:

| Defect | Description | Possible cause | Fix direction |
|---|---|---|---|
| plastic_skin | skin looks waxy, airbrushed, no tonal variation | too much smoothing, high beauty strength | reduce strength, add natural variation, crop check |
| glassy_eyes | eyes look wet/glass/artificial | prompt, enhancer, video model | preserve eyes, reduce eye transformation |
| rubber_lips | lips lose texture and natural edge | over-enhancement, bad animation | reduce mouth/lip manipulation |
| beard_artifacts | beard looks painted or flickers | poor base avatar or video model | better still, crop refinement |
| identity_drift | face changes across passes | too much regeneration | lower transformation strength, use selected still |
| overbeautified | looks like generic AI influencer | prompt/style too generic | more specific character brief |
| ashy_skin | dark/warm skin becomes gray or washed out | wrong color correction, over-lighting | tone-safe correction |
| video_face_slip | face slides or morphs in video | weak still, strong motion | improve still, reduce motion prompt |

---

## 19. Scoring system

Использовать шкалу 1-5:

1. Плохо, непригодно.
2. Есть заметные дефекты.
3. Приемлемо для эксперимента, но не для портфолио.
4. Хорошо, можно показывать в кейсе.
5. Отлично, почти commercial-ready.

Критерии для still image:

- skin_realism;
- eye_realism;
- lips_realism;
- hair_beard_realism;
- identity_consistency;
- overall_score.

Критерии для video:

- face_stability;
- eye_stability;
- lips_stability;
- skin_stability;
- identity_consistency;
- overall_score.

---

## 20. Скрипты, которые должен создать Codex

### 20.1. `scripts/register_dataset.py`

Назначение:

- сканировать `02_source_data/`;
- находить изображения;
- присваивать `image_id`;
- создавать или обновлять `dataset_register.csv`;
- не перезаписывать ручные поля.

### 20.2. `scripts/make_contact_sheet.py`

Назначение:

- создавать overview grid по выбранным изображениям;
- сохранять в `06_analysis/contact_sheets/`.

### 20.3. `scripts/make_comparison_grid.py`

Назначение:

- создавать сравнения:
  - base avatar;
  - realism pass;
  - final still;
- добавлять подписи;
- сохранять в `06_analysis/comparison_grids/` и `07_report/assets/images/`.

### 20.4. `scripts/extract_face_crops.py`

Назначение:

- делать ручные или полуавтоматические crop-зоны;
- зоны:
  - skin;
  - eyes;
  - lips;
  - hair/beard;
- сохранять crop в `06_analysis/crops/`.

### 20.5. `scripts/lab_color_stats.py`

Назначение:

- считать простую LAB/HSV статистику по crop-изображениям;
- сохранять CSV;
- помогать видеть пересвет, ashy effect, потерю chroma.

### 20.6. `scripts/build_html_report.py`

Назначение:

- брать `07_report/report.md`;
- подключать assets;
- собирать `07_report/report.html`;
- создавать аккуратный self-contained или static-friendly HTML.

### 20.7. `scripts/validate_project_structure.py`

Назначение:

- проверять наличие обязательных папок;
- проверять наличие CSV;
- проверять битые ссылки в отчете;
- выводить список missing items.

---

## 21. План на 14 дней

### День 1. Создание структуры

Задачи:

- создать репозиторий;
- добавить `PROJECT_BRIEF.md`;
- создать `AGENTS.md`;
- создать структуру папок;
- создать `requirements.txt`;
- создать `.gitignore`;
- создать пустые CSV-регистры.

Результат:

- проект готов к работе с Codex.

### День 2. Источники и references

Задачи:

- собрать 20-30 публичных reference images;
- добавить 5-10 PPR10K examples, если удобно;
- добавить 3-6 generated reference images;
- заполнить `dataset_register.csv`.

Результат:

- есть контролируемый набор исходных данных.

### День 3. Character briefs

Задачи:

- создать два character profiles;
- прописать визуальные цели и риски;
- создать prompts для генерации базовых аватаров.

Результат:

- `avatar_a_mens_grooming` и `avatar_b_skincare_creator` готовы к генерации.

### День 4. Base avatars

Задачи:

- сгенерировать 3-5 candidates для каждого аватара;
- выбрать по 1 основному варианту;
- заполнить `base_avatar_register.csv`.

Результат:

- есть selected base avatar для каждого кейса.

### День 5. Диагностика базовых аватаров

Задачи:

- сделать crop-зоны;
- описать дефекты;
- заполнить observations.

Результат:

- понятно, что нужно улучшать.

### День 6-7. Realism passes

Задачи:

- сделать skin realism pass;
- сделать eyes pass;
- сделать lips pass;
- для men's grooming сделать hair/beard pass;
- сохранить все варианты;
- заполнить `realism_run_log.csv`.

Результат:

- есть улучшенные still images.

### День 8. Comparison grids

Задачи:

- сделать comparison grids:
  - base;
  - improved;
  - final;
- сделать crop comparisons.

Результат:

- визуальные материалы готовы для отчета.

### День 9-10. Image-to-video test

Задачи:

- выбрать лучший final still;
- сделать 1 короткий video test на каждого аватара;
- оценить стабильность лица, глаз, губ и кожи;
- заполнить `video_test_log.csv`.

Результат:

- есть доказательство, как still quality влияет на video readiness.

### День 11. Анализ результатов

Задачи:

- обновить `observations.md`;
- описать failure modes;
- сформировать выводы.

Результат:

- есть аналитическая часть кейса.

### День 12. Report draft

Задачи:

- написать `07_report/report.md`;
- добавить изображения и таблицы;
- описать ограничения.

Результат:

- есть черновик кейса.

### День 13. HTML report

Задачи:

- собрать `report.html`;
- проверить адаптивность;
- проверить ссылки и assets.

Результат:

- кейс готов к локальному просмотру.

### День 14. Publication package

Задачи:

- подготовить `08_site/index.html`;
- оптимизировать изображения;
- проверить, нет ли приватных данных;
- подготовить публикацию через GitHub Pages или другой static hosting.

Результат:

- кейс готов к публикации.

---

## 22. Структура финального отчета

Файл: `07_report/report.md`

Рекомендуемая структура:

```md
# AI UGC Avatar Realism Pipeline for Beauty & Grooming Brands

## 1. Goal

## 2. Why this case matters

## 3. Target niches
- Men's grooming
- Sensorial skincare

## 4. Method
- Character brief
- Base avatar generation
- Realism pass
- Crop inspection
- Image-to-video test

## 5. Avatar A: Men's Grooming Advisor
- Character profile
- Base avatar
- Visual defects
- Realism improvements
- Video test
- Result

## 6. Avatar B: Skincare Routine Creator
- Character profile
- Base avatar
- Visual defects
- Realism improvements
- Video test
- Result

## 7. Failure modes

## 8. What worked

## 9. What did not work

## 10. Tooling notes

## 11. Limitations

## 12. Next steps
```

---

## 23. Публикация сайта

### 23.1. Минимальный вариант

Использовать GitHub Pages.

Требования:

- создать `08_site/index.html`;
- положить assets в `08_site/assets/`;
- убедиться, что нет приватных файлов;
- включить GitHub Pages для репозитория;
- публиковать из branch или `/docs`, если так удобнее.

### 23.2. Альтернатива

Можно использовать:

- Vercel;
- Netlify;
- Cloudflare Pages;
- собственный статический сайт.

Для первого кейса GitHub Pages достаточно.

### 23.3. Что нельзя публиковать

Не публиковать:

- приватные фото;
- чужие изображения с непонятной лицензией;
- API keys;
- `.env`;
- raw datasets;
- большие модели;
- коммерческие ассеты без разрешения;
- сомнительные before/after с реальными людьми в унизительном контексте.

---

## 24. AGENTS.md для Codex

Codex должен создать отдельный файл `AGENTS.md` со следующим содержанием:

```md
# AGENTS.md

## Project
AI UGC Avatar Realism Case for Beauty & Grooming Brands.

## Goal
Build a personal case study showing a structured AI avatar realism pipeline for beauty, skincare and men's grooming UGC use cases.

The final output is a publishable static HTML case study with character briefs, base avatars, realism passes, crop analysis, short video tests, observations and limitations.

## Working principles
- Do not overwrite source images.
- Keep raw data, generated media, analysis assets, workflows and reports separated.
- Every important experiment must be traceable through CSV logs.
- Prefer small, readable Python scripts over complex frameworks.
- Do not add unnecessary dependencies.
- Do not invent results. Only reference files that exist in the project.
- Do not commit API keys, model files, paid assets or private images.
- When generating reports, include limitations and failed experiments.
- Preserve a clear distinction between known facts, observations and assumptions.

## Tech stack
- Python 3.11
- pandas
- Pillow
- OpenCV
- scikit-image
- Jinja2
- Markdown
- HTML/CSS for final report
- Optional ComfyUI workflows

## Folder rules
- 00_project_control: project decisions, roadmap, references
- 01_character_briefs: avatar profiles and prompts
- 02_source_data: source images and dataset register
- 03_base_avatars: generated avatar candidates and selected stills
- 04_realism_passes: skin/eyes/lips/hair-beard passes
- 05_video_tests: image-to-video inputs, outputs and observations
- 06_analysis: crops, comparison grids, visual defect taxonomy, stats
- 07_report: final Markdown/HTML case report
- 08_site: publication-ready static site
- 09_workflows: ComfyUI workflows and external tool notes
- scripts: Python utilities

## Definition of done
A task is done only when:
- the requested files are created in the correct folder;
- scripts run without errors;
- README or relevant notes are updated;
- no source images are modified;
- generated outputs are traceable in CSV logs.
```

---

## 25. Первый prompt для Codex

Использовать этот prompt после создания папки проекта и добавления `PROJECT_BRIEF.md`:

```text
Read PROJECT_BRIEF.md carefully.

Create the initial repository structure for this project.

Tasks:
1. Create all folders described in section 8.
2. Create AGENTS.md using the content from section 24.
3. Create README.md with a concise project overview, goals, expected deliverables and local setup instructions.
4. Create requirements.txt with the Python dependencies from section 12.
5. Create .gitignore based on section 10.
6. Create empty CSV files with headers:
   - 02_source_data/dataset_register.csv
   - 03_base_avatars/base_avatar_register.csv
   - 04_realism_passes/realism_run_log.csv
   - 05_video_tests/video_test_log.csv
7. Create placeholder Markdown files:
   - 00_project_control/project_goal.md
   - 00_project_control/decisions.md
   - 00_project_control/open_questions.md
   - 00_project_control/roadmap.md
   - 00_project_control/references.md
   - 06_analysis/visual_defect_taxonomy.md
   - 06_analysis/observations.md
   - 07_report/report.md
   - 07_report/publish_checklist.md
8. Create scripts/validate_project_structure.py that checks required folders and files.

Keep everything simple and transparent.
Do not add unnecessary frameworks.
Do not create fake results.
Do not download images or models yet.
After creating files, run the validation script and show the result.
```

---

## 26. Второй prompt для Codex

После структуры проекта:

```text
Implement scripts/register_dataset.py.

Requirements:
- Scan 02_source_data/public_references, 02_source_data/generated_references and 02_source_data/own_test_images.
- Detect image files: jpg, jpeg, png, webp.
- Create or update 02_source_data/dataset_register.csv.
- Use stable image_id values based on source folder and filename.
- Preserve existing manual labels if the CSV already exists.
- Add missing rows for new images.
- Do not delete rows automatically.
- Add columns exactly as defined in PROJECT_BRIEF.md section 16.1.
- Print a short summary: images found, rows added, rows preserved.
```

---

## 27. Третий prompt для Codex

После добавления первых изображений:

```text
Implement scripts/make_contact_sheet.py.

Requirements:
- Read 02_source_data/dataset_register.csv.
- Select images where allowed_for_public_report is yes or where use_case is not empty.
- Create a contact sheet with thumbnails, image_id, source, skin_tone, lighting and use_case.
- Save the output to 06_analysis/contact_sheets/contact_sheet_001.jpg.
- Do not modify source images.
- Use Pillow only unless OpenCV is necessary.
```

---

## 28. Четвертый prompt для Codex

После появления base/final images:

```text
Implement scripts/make_comparison_grid.py.

Requirements:
- Create comparison grids for avatar outputs.
- Input: avatar_id and a list of image paths for base, realism pass and final still.
- Output: labeled comparison image saved to 06_analysis/comparison_grids and copied to 07_report/assets/images.
- Support 2-column and 3-column layouts.
- Add clear labels under each image.
- Keep aspect ratios consistent.
- Do not overwrite existing outputs unless --overwrite is passed.
```

---

## 29. Пятый prompt для Codex

Для отчета:

```text
Implement scripts/build_html_report.py.

Requirements:
- Read 07_report/report.md.
- Convert it to 07_report/report.html.
- Use a simple local CSS template.
- Copy required assets from 07_report/assets to 08_site/assets.
- Generate 08_site/index.html for publication.
- Do not use external CDN.
- The final site must work by opening 08_site/index.html locally.
```

---

## 30. Риски проекта и как их снижать

### Риск 1. Проект расползется

Решение:

- держать первый scope: 2 аватара, 1-2 видео, 1 HTML-отчет;
- не уходить в обучение LoRA и SaaS.

### Риск 2. MacBook Air будет медленным

Решение:

- использовать Mac как control center;
- тяжелые этапы делать через веб-сервисы или cloud GPU;
- локально делать анализ и отчетность.

### Риск 3. Результат будет выглядеть слишком AI

Решение:

- делать crop-анализ;
- улучшать still до video;
- не использовать чрезмерно глянцевые beauty prompts;
- оценивать eyes/skin/lips отдельно.

### Риск 4. Публикационные права

Решение:

- использовать только разрешенные источники;
- сохранять license notes;
- для спорных изображений ставить `allowed_for_public_report = no`;
- для публичного отчета использовать собственные generated assets или clearly licensed references.

### Риск 5. Слишком много инструментов

Решение:

- проектировать pipeline tool-agnostic;
- фиксировать не только инструмент, но и этап:
  - base generation;
  - skin pass;
  - eye pass;
  - lips pass;
  - video test.

---

## 31. Roadmap развития после первого кейса

### Версия 1.0

- 2 аватара;
- still realism passes;
- 1-2 коротких video tests;
- HTML case study.

### Версия 1.1

- добавить 3-й аватар для fragrance/body care;
- добавить более строгий scoring;
- добавить comparison sliders в HTML;
- добавить better video embedding.

### Версия 1.2

- добавить ComfyUI workflow более глубоко;
- попробовать Z-Image / Flux / LoRA tuning;
- добавить автоматический crop detection.

### Версия 2.0

- mini landing page для услуги:
  - AI UGC Avatar Realism Tuning;
  - Beauty / Skincare / Grooming content systems;
  - before/after examples;
  - contact form.

### Версия 3.0

- MVP сервиса:
  - загрузка character brief;
  - генерация аватара;
  - визуальный QA checklist;
  - экспорт UGC video pack.

---

## 32. Источники и справочные ссылки

В этом разделе хранить ссылки на официальные источники и документацию.

Рекомендуемые стартовые ссылки:

- ComfyUI macOS Desktop documentation: https://docs.comfy.org/installation/desktop/macos
- ComfyUI system requirements: https://docs.comfy.org/installation/system_requirements
- Codex CLI GitHub: https://github.com/openai/codex
- Codex AGENTS.md guide: https://developers.openai.com/codex/guides/agents-md
- AGENTS.md open format: https://agents.md/
- Homebrew: https://brew.sh/
- Homebrew Installation: https://docs.brew.sh/Installation
- Pexels License: https://www.pexels.com/license/
- Unsplash License: https://unsplash.com/license
- PPR10K dataset: https://github.com/csjliang/PPR10K
- GitHub Pages: https://pages.github.com/
- GitHub Pages docs: https://docs.github.com/pages

---

## 33. Финальный Definition of Done

Проект завершен, если выполнены условия:

1. `README.md` объясняет проект за 1-2 минуты.
2. `AGENTS.md` помогает Codex работать без хаоса.
3. Структура папок создана и валидируется скриптом.
4. Есть минимум 2 character profiles.
5. Есть минимум 2 base avatars.
6. Есть минимум 2 final stills после realism passes.
7. Есть crop-сравнения зон лица.
8. Есть минимум 1 video test.
9. Есть `realism_run_log.csv` и `video_test_log.csv`.
10. Есть `07_report/report.html`.
11. Есть publication-ready `08_site/index.html`.
12. В отчете есть honest limitations.
13. Нет приватных ключей, чужих закрытых данных и тяжелых моделей в репозитории.
14. Кейс можно открыть локально и показать другому человеку.

---

## 34. Главное правило проекта

Не доказывать, что AI может все.

Доказывать другое:

> AI visual content становится коммерчески полезным только тогда, когда есть управляемый pipeline, визуальная диагностика, контроль дефектов, traceability экспериментов и честная проверка результата.

Именно это должен показать проект.

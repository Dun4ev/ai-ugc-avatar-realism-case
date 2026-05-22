# AGENTS.md

## Проект
AI UGC Avatar Realism Case for Beauty & Grooming Brands.

## Цель
Создать личный кейс, который показывает структурированный pipeline повышения реалистичности AI-аватаров для beauty, skincare и men's grooming UGC-сценариев.

Финальный результат: публикуемый статический HTML-кейс с character briefs, базовыми аватарами, realism passes, crop-анализом, короткими video tests, наблюдениями и ограничениями.

## Принципы работы
- Не перезаписывать исходные изображения.
- Разделять raw data, generated media, analysis assets, workflows и reports.
- Каждый важный эксперимент должен быть отслеживаемым через CSV-логи.
- Предпочитать небольшие читаемые Python-скрипты сложным фреймворкам.
- Не добавлять лишние зависимости.
- Не выдумывать результаты. Ссылаться только на файлы, которые реально есть в проекте.
- Не коммитить API keys, model files, paid assets или private images.
- В отчетах указывать limitations и failed experiments.
- Явно разделять известные факты, наблюдения и предположения.

## Технический стек
- Python 3.11
- pandas
- Pillow
- OpenCV
- scikit-image
- Jinja2
- Markdown
- HTML/CSS для финального отчета
- Опционально: ComfyUI workflows

## Правила папок
- 00_project_control: решения, roadmap, references.
- 01_character_briefs: профили аватаров и prompts.
- 02_source_data: исходные изображения и dataset register.
- 03_base_avatars: generated avatar candidates и selected stills.
- 04_realism_passes: skin/eyes/lips/hair-beard passes.
- 05_video_tests: image-to-video inputs, outputs и observations.
- 06_analysis: crops, comparison grids, visual defect taxonomy, stats.
- 07_report: финальный Markdown/HTML case report.
- 08_site: publication-ready static site.
- 09_workflows: ComfyUI workflows и external tool notes.
- scripts: Python-утилиты.

## Definition of Done
Задача считается завершенной только если:
- запрошенные файлы созданы в правильной папке;
- скрипты запускаются без ошибок;
- README или релевантные notes обновлены;
- исходные изображения не изменены;
- generated outputs отслеживаются через CSV-логи.

# AI UGC Avatar Realism Case

Personal case study for designing and documenting an AI avatar realism pipeline for beauty, skincare and men's grooming UGC use cases.

The project focuses on making AI-generated avatar stills more suitable for short UGC-style video tests by inspecting and improving skin, eyes, lips, hair and beard realism before image-to-video generation.

## Goals

- Create two AI avatar case tracks: men's grooming and skincare routine creator.
- Document character briefs, base avatar candidates, realism passes and visual defects.
- Track important experiments through CSV logs.
- Build a final Markdown and HTML report that can be published as a static case study.
- Keep limitations, failed experiments and source rights visible.

## Expected deliverables

- Structured project repository.
- Character profiles in Markdown and JSON.
- Base and improved avatar stills.
- Crop comparisons for key face zones.
- Short image-to-video tests.
- Experiment logs in CSV.
- Final `07_report/report.html`.
- Publication-ready `08_site/index.html`.

## Local setup

Create a virtual environment and install dependencies only when scripts are needed:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Validate the current scaffold:

```bash
python3 scripts/validate_project_structure.py
```

Register source images after adding files to `02_source_data/`:

```bash
python3 scripts/register_dataset.py
```

## Project rules

- Do not overwrite source images.
- Keep source materials under `02_source_data/`.
- Keep generated outputs separate from source files.
- Do not commit private images, API keys, model files or heavy raw media.
- Do not invent results in reports. Reference only files that exist.

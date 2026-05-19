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

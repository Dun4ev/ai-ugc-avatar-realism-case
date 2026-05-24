#!/usr/bin/env python3
"""Build a static HTML report and publication index from report.md."""

from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "07_report"
SITE_DIR = ROOT / "08_site"
DEFAULT_INPUT = REPORT_DIR / "report.md"
DEFAULT_REPORT_HTML = REPORT_DIR / "report.html"
DEFAULT_SITE_INDEX = SITE_DIR / "index.html"


CSS = """
:root {
  color-scheme: light;
  --text: #23282d;
  --muted: #69737d;
  --line: #d8dde2;
  --soft: #f4f7f8;
  --surface: #ffffff;
  --accent: #276365;
  --accent-2: #b65f52;
  --ink: #172024;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: var(--text);
  background:
    linear-gradient(135deg, rgba(39, 99, 101, 0.10), rgba(182, 95, 82, 0.08) 42%, rgba(244, 247, 248, 0.92) 78%),
    #f7f9fa;
  line-height: 1.55;
}

body::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  background-image:
    linear-gradient(rgba(23, 32, 36, 0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(23, 32, 36, 0.03) 1px, transparent 1px);
  background-size: 44px 44px;
  mask-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.7), transparent 62%);
}

main {
  position: relative;
  max-width: 1120px;
  margin: 0 auto;
  padding: 42px 28px 76px;
}

h1, h2, h3 {
  line-height: 1.18;
  letter-spacing: 0;
}

h1 {
  margin: 0 0 22px;
  max-width: 900px;
  color: var(--ink);
  font-size: 46px;
  font-weight: 760;
}

h2 {
  margin: 48px 0 16px;
  padding: 18px 0 0;
  border-top: 1px solid rgba(39, 99, 101, 0.22);
  color: var(--ink);
  font-size: 24px;
  font-weight: 720;
}

h3 {
  margin: 28px 0 10px;
  color: var(--ink);
  font-size: 18px;
  font-weight: 700;
}

p, ul, ol, .table-wrap {
  margin: 0 0 16px;
}

p {
  max-width: 840px;
}

ul, ol {
  padding-left: 24px;
}

li {
  margin: 4px 0;
}

a {
  color: var(--accent);
  font-weight: 600;
  text-underline-offset: 3px;
}

code {
  padding: 2px 6px;
  border: 1px solid rgba(39, 99, 101, 0.13);
  border-radius: 5px;
  background: rgba(39, 99, 101, 0.08);
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.92em;
}

img {
  display: block;
  max-width: 100%;
  height: auto;
  margin: 18px 0 28px;
  border: 1px solid rgba(23, 32, 36, 0.12);
  border-radius: 8px;
  background: #ffffff;
  box-shadow: 0 18px 45px rgba(23, 32, 36, 0.12);
}

video {
  display: block;
  width: min(100%, 520px);
  height: auto;
  margin: 18px 0 28px;
  border: 1px solid rgba(23, 32, 36, 0.16);
  border-radius: 8px;
  background: #000000;
  box-shadow: 0 18px 45px rgba(23, 32, 36, 0.14);
}

table {
  min-width: 100%;
  width: 100%;
  margin: 0;
  border-collapse: collapse;
  border: 0;
  background: var(--surface);
  font-size: 14px;
}

.table-wrap {
  width: 100%;
  max-width: 100%;
  overflow-x: auto;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--surface);
  box-shadow: 0 10px 28px rgba(23, 32, 36, 0.06);
}

th, td {
  padding: 10px 12px;
  border-bottom: 1px solid var(--line);
  vertical-align: top;
  overflow-wrap: anywhere;
}

td + td,
th + th {
  border-left: 1px solid rgba(216, 221, 226, 0.75);
}

th {
  background: #eaf2f1;
  text-align: left;
  color: var(--ink);
  font-weight: 700;
}

tr:last-child td {
  border-bottom: 0;
}

tbody tr:nth-child(even) {
  background: #fafbfb;
}

td code,
th code {
  white-space: normal;
  overflow-wrap: anywhere;
  word-break: break-word;
}

.meta {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 18px;
  padding: 7px 11px;
  border: 1px solid rgba(39, 99, 101, 0.20);
  border-radius: 999px;
  color: #315d60;
  background: rgba(255, 255, 255, 0.68);
  backdrop-filter: blur(12px);
  font-size: 14px;
  font-weight: 650;
}

.hero {
  margin: 0 0 34px;
  padding: 30px 32px 34px;
  border: 1px solid rgba(23, 32, 36, 0.10);
  border-radius: 8px;
  background:
    linear-gradient(120deg, rgba(255, 255, 255, 0.96), rgba(234, 242, 241, 0.92)),
    var(--surface);
  box-shadow: 0 24px 70px rgba(23, 32, 36, 0.11);
}

.hero-kicker {
  margin: 0 0 12px;
  color: var(--accent-2);
  font-size: 13px;
  font-weight: 760;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.hero-subtitle {
  max-width: 780px;
  margin: 0;
  color: var(--muted);
  font-size: 18px;
}

.content {
  padding: 30px 32px 38px;
  border: 1px solid rgba(23, 32, 36, 0.10);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.92);
  box-shadow: 0 18px 58px rgba(23, 32, 36, 0.08);
}

@media (max-width: 700px) {
  main { padding: 24px 14px 52px; }
  .hero,
  .content { padding: 22px 18px 28px; }
  h1 { font-size: 31px; }
  h2 { font-size: 21px; }
  .hero-subtitle { font-size: 16px; }
  table { min-width: 680px; }
}
""".strip()


def is_video_src(src: str) -> bool:
    return src.lower().split("?", 1)[0].endswith((".mp4", ".webm", ".mov", ".m4v"))


def media_to_html(alt: str, src: str) -> str:
    escaped_alt = html.escape(alt)
    escaped_src = html.escape(src, quote=True)
    if is_video_src(src):
        return f'<video controls preload="metadata" src="{escaped_src}">{escaped_alt}</video>'
    return f'<img src="{escaped_src}" alt="{escaped_alt}">'


def inline_markdown(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", lambda match: media_to_html(match.group(1), match.group(2)), escaped)
    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', escaped)
    return escaped


def is_table_block(lines: list[str], index: int) -> bool:
    return (
        index + 1 < len(lines)
        and lines[index].strip().startswith("|")
        and lines[index + 1].strip().startswith("|")
        and set(lines[index + 1].strip().replace("|", "").replace(":", "").replace(" ", "")) <= {"-"}
    )


def table_to_html(lines: list[str], index: int) -> tuple[str, int]:
    table_lines = []
    while index < len(lines) and lines[index].strip().startswith("|"):
        table_lines.append(lines[index].strip())
        index += 1

    def cells(line: str) -> list[str]:
        return [cell.strip() for cell in line.strip("|").split("|")]

    header = cells(table_lines[0])
    body = [cells(line) for line in table_lines[2:]]
    parts = ["<table>", "<thead><tr>"]
    parts.extend(f"<th>{inline_markdown(cell)}</th>" for cell in header)
    parts.append("</tr></thead>")
    parts.append("<tbody>")
    for row in body:
        parts.append("<tr>")
        parts.extend(f"<td>{inline_markdown(cell)}</td>" for cell in row)
        parts.append("</tr>")
    parts.append("</tbody></table>")
    return '<div class="table-wrap">\n' + "\n".join(parts) + "\n</div>", index


def list_to_html(lines: list[str], index: int, ordered: bool) -> tuple[str, int]:
    tag = "ol" if ordered else "ul"
    parts = [f"<{tag}>"]
    pattern = re.compile(r"^\d+\.\s+") if ordered else re.compile(r"^-\s+")
    while index < len(lines) and pattern.match(lines[index].strip()):
        item = pattern.sub("", lines[index].strip())
        parts.append(f"<li>{inline_markdown(item)}</li>")
        index += 1
    parts.append(f"</{tag}>")
    return "\n".join(parts), index


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    parts: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index].rstrip()
        stripped = line.strip()

        if not stripped:
            index += 1
            continue

        media_match = re.fullmatch(r"!\[([^\]]*)\]\(([^)]+)\)", stripped)
        if media_match:
            parts.append(media_to_html(media_match.group(1), media_match.group(2)))
            index += 1
            continue

        if is_table_block(lines, index):
            table_html, index = table_to_html(lines, index)
            parts.append(table_html)
            continue

        if stripped.startswith("# "):
            parts.append(f"<h1>{inline_markdown(stripped[2:])}</h1>")
        elif stripped.startswith("## "):
            parts.append(f"<h2>{inline_markdown(stripped[3:])}</h2>")
        elif stripped.startswith("### "):
            parts.append(f"<h3>{inline_markdown(stripped[4:])}</h3>")
        elif stripped.startswith("- "):
            list_html, index = list_to_html(lines, index, ordered=False)
            parts.append(list_html)
            continue
        elif re.match(r"^\d+\.\s+", stripped):
            list_html, index = list_to_html(lines, index, ordered=True)
            parts.append(list_html)
            continue
        else:
            parts.append(f"<p>{inline_markdown(stripped)}</p>")

        index += 1

    return "\n".join(parts)


def build_document(title: str, body_html: str) -> str:
    first_heading_pattern = re.compile(r"^<h1>(.*?)</h1>\n?", re.DOTALL)
    first_heading = first_heading_pattern.search(body_html)
    rendered_title = first_heading.group(1) if first_heading else html.escape(title)
    content_html = first_heading_pattern.sub("", body_html, count=1).strip()

    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="icon" href="data:,">
  <style>{CSS}</style>
</head>
<body>
  <main>
    <section class="hero">
      <div class="meta">AI UGC Avatar Realism Case · static report</div>
      <div class="hero-kicker">Beauty · Grooming · UGC Avatars</div>
      <h1>{rendered_title}</h1>
      <p class="hero-subtitle">Structured realism pipeline with source tracking, ON1 passes, crop analysis, scoring and Magnific/Kling video tests.</p>
    </section>
    <article class="content">
      {content_html}
    </article>
  </main>
</body>
</html>
"""


def copy_assets(report_dir: Path, site_dir: Path) -> None:
    source_assets = report_dir / "assets"
    target_assets = site_dir / "assets"
    if target_assets.exists():
        shutil.rmtree(target_assets)
    if source_assets.exists():
        shutil.copytree(source_assets, target_assets)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build report.html and 08_site/index.html from report.md.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Input Markdown report.")
    parser.add_argument("--report-html", type=Path, default=DEFAULT_REPORT_HTML, help="Output report HTML.")
    parser.add_argument("--site-index", type=Path, default=DEFAULT_SITE_INDEX, help="Output site index HTML.")
    args = parser.parse_args()

    input_path = args.input if args.input.is_absolute() else ROOT / args.input
    report_html = args.report_html if args.report_html.is_absolute() else ROOT / args.report_html
    site_index = args.site_index if args.site_index.is_absolute() else ROOT / args.site_index

    if not input_path.is_file():
        print(f"ERROR: input report not found: {input_path}", file=sys.stderr)
        return 1

    markdown = input_path.read_text(encoding="utf-8")
    title = next((line.strip("# ").strip() for line in markdown.splitlines() if line.startswith("# ")), "Report")
    body_html = markdown_to_html(markdown)
    document = build_document(title, body_html)

    report_html.parent.mkdir(parents=True, exist_ok=True)
    site_index.parent.mkdir(parents=True, exist_ok=True)
    report_html.write_text(document, encoding="utf-8")

    copy_assets(REPORT_DIR, SITE_DIR)
    site_document = document.replace('src="assets/', 'src="assets/')
    site_index.write_text(site_document, encoding="utf-8")

    print(f"Report HTML written: {report_html.relative_to(ROOT)}")
    print(f"Site index written: {site_index.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

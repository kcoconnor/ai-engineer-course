"""Build the HTML presentations from the Marp Markdown decks.

The Markdown in slides/ is the source. Edit it there, then run from the repository root:

    python3 tools/build_html_decks.py   # build presentations/ (not committed; GitHub Pages builds it on each push to main)

Requires Node.js (npx). The Marp CLI version is pinned so the output is the same on every machine.
"""
import html
import pathlib
import re
import shutil
import subprocess
import sys

MARP = ["npx", "-y", "@marp-team/marp-cli@4.5.1"]
ROOT = pathlib.Path(__file__).resolve().parent.parent
SLIDES = ROOT / "slides"
OUT = ROOT / "presentations"

GROUPS = [
    ("Module 1 – Strategy", "m1-"),
    ("Module 2 – Design", "m2-"),
    ("Module 3 – Systems", "m3-"),
    ("Module 4 – Engineering", "m4-"),
    ("Review sessions", "review-"),
]


def decks():
    return sorted(p for p in SLIDES.glob("*.md") if p.name != "README.md")


def title(deck):
    """First heading after the front matter, for example 'Session 1.2 · ...'."""
    first_slide = deck.read_text().split("\n---\n", 2)[1]
    h1 = re.search(r"^#\s+(.+)$", first_slide, re.M)
    session = re.search(r"^##\s+(Session \d+\.\d+)", first_slide, re.M)
    name = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else deck.stem
    return f"{session.group(1)}: {name}" if session else name


def index_html(items):
    parts = []
    for name, prefix in GROUPS:
        rows = [d for d in items if d.name.startswith(prefix)]
        if not rows:
            continue
        lis = "\n".join(
            f'      <li><a href="{d.stem}.html">{html.escape(title(d))}</a> <span class="file">{d.stem}</span></li>'
            for d in rows
        )
        parts.append(f"    <h2>{html.escape(name)}</h2>\n    <ul>\n{lis}\n    </ul>")
    groups = "\n".join(parts)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AI Engineering: presentations</title>
  <style>
    body {{ font-family: system-ui, sans-serif; max-width: 860px; margin: 40px auto; padding: 0 20px; color: #222; }}
    h1, h2 {{ color: #1f3a5f; }}
    li {{ margin: 6px 0; }}
    .file {{ color: #888; font-size: 0.85em; margin-left: 8px; }}
    .help {{ background: #f3f6fa; padding: 12px 16px; border-radius: 6px; }}
  </style>
</head>
<body>
  <h1>AI Engineering: presentations</h1>
  <p class="help">Open a deck and press <b>F</b> for full screen. Use the arrow keys to move. Press <b>P</b> for presenter view with speaker notes and a timer.
  These files are generated from <code>slides/*.md</code>. Do not edit them.</p>
{groups}
</body>
</html>
"""


def build(target):
    target.mkdir(parents=True, exist_ok=True)
    items = decks()
    for d in items:
        subprocess.run(MARP + [str(d), "-o", str(target / f"{d.stem}.html")],
                       check=True, cwd=ROOT, capture_output=True)
    (target / "index.html").write_text(index_html(items))
    return items


def main():
    # The review decks are generated from reviews/*.md first.
    subprocess.run([sys.executable, str(ROOT / "tools" / "build_review_decks.py")], check=True, cwd=ROOT,
                   capture_output=True)
    if OUT.exists():
        shutil.rmtree(OUT)
    items = build(OUT)
    print(f"built {len(items)} decks + index.html into presentations/")


if __name__ == "__main__":
    main()

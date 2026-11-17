"""Generate the profile's SVG cards, tech-stack panel and dividers.

Run from the repo root:  python tools/make_assets.py
Edit PROJECTS or STACK below, re-run, and commit the changed SVGs.
"""

from html import escape
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
FONT = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"

PROJECTS = [
    ("az900", "AZ-900 Study Buddy", "Azure exam prep in English, Kiswahili and Sheng, with Kenyan examples, original quizzes and a free AI tutor.", ["JavaScript", "FastAPI", "Gemini"], ("#5b1f6e", "#c2396d")),
    ("savannah", "Savannah Loan System", "Harvest-aware, bias-audited loan decisions for informal market vendors in East Africa.", ["React", "TypeScript", "AI ethics"], ("#c2396d", "#ff7a59")),
    ("kiroween", "The Haunted Portfolio", "My Kiroween 2026 hackathon entry: a spooky haunted-mansion developer portfolio.", ["HTML", "CSS", "JavaScript"], ("#1e0b3b", "#6a2380")),
    ("northstar", "NorthStar Webhook", "A FastAPI webhook receiver with a chat-style tester, live on Render. Built on Day 1 of an industry sprint.", ["Python", "FastAPI", "Webhooks"], ("#8c2f6a", "#ff7a59")),
    ("system-design", "QuickNotes System Design", "A notes service designed for 1 million users: REST API, PostgreSQL model and scalable architecture.", ["System design", "PostgreSQL", "REST"], ("#3a1650", "#8c2f6a")),
    ("solstice", "Solstice Kiosk", "An event check-in kiosk that swaps polling for an asynchronous webhook flow.", ["Python", "FastAPI", "Webhooks"], ("#b8326a", "#ef6a55")),
    ("quicknotes", "QuickNotes", "A fast notes app with categories, search and local saving, usable by keyboard and screen reader.", ["JavaScript", "CSS", "Accessibility"], ("#d9533f", "#f28a4c")),
    ("chat-cartographer", "Chat Cartographer", "A Twitch chat overlay that maps viewer theories, discoveries and running jokes.", ["JavaScript", "Twitch", "Overlay"], ("#2a0f36", "#7a2d8a")),
]

STACK = [
    ("Languages", ["Python", "JavaScript", "TypeScript", "SQL", "HTML", "CSS"]),
    ("Backend", ["FastAPI", "Pydantic", "pytest", "PostgreSQL", "Prisma", "REST APIs"]),
    ("Frontend", ["React", "TanStack", "Tailwind CSS", "Accessibility"]),
    ("Cloud & tools", ["Azure (AZ-900)", "GitHub Actions", "GitHub Pages", "Render", "Gemini API", "Git"]),
]

ACACIA = (
    '<path d="M24 60 L26 34 L18 26 L21 24 L28 31 L29 20 L32 20 L31 32 L38 25 L41 27 L33 35 L31 60 Z"/>'
    '<path d="M4 26 C 12 16, 30 15, 38 18 C 46 15, 62 17, 66 25 C 56 30, 42 28, 36 28 C 26 31, 12 31, 4 26 Z"/>'
)


def text_width(text: str, size: float) -> float:
    """Rough width of a sans-serif string, good enough for chip sizing."""
    return len(text) * size * 0.56


def chips(items, x, y, size=12.5, gap=8, fill="#ffffff", fill_opacity=0.18, color="#ffffff"):
    out = []
    for item in items:
        w = text_width(item, size) + 22
        out.append(
            f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="26" rx="13" fill="{fill}" fill-opacity="{fill_opacity}"/>'
            f'<text x="{x + w / 2:.1f}" y="{y + 17.5}" font-size="{size}" font-weight="600" fill="{color}" text-anchor="middle">{escape(item)}</text>'
        )
        x += w + gap
    return "".join(out), x


def project_card(key, title, desc, tags, colors):
    start, end = colors
    lines = textwrap.wrap(desc, 46)[:3]
    desc_svg = "".join(
        f'<text x="28" y="{98 + i * 22}" font-size="15.5" fill="#ffffff" fill-opacity="0.92">{escape(line)}</text>'
        for i, line in enumerate(lines)
    )
    chip_svg, _ = chips(tags, 28, 166)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 214" width="440" height="214" role="img" aria-label="{escape(title)}: {escape(desc)}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{start}"/>
      <stop offset="1" stop-color="{end}"/>
    </linearGradient>
    <radialGradient id="sun" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ffe3a3" stop-opacity="0.55"/>
      <stop offset="1" stop-color="#ffe3a3" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="c"><rect width="440" height="214" rx="18"/></clipPath>
  </defs>
  <g clip-path="url(#c)" font-family="{FONT}">
    <rect width="440" height="214" fill="url(#bg)"/>
    <circle cx="392" cy="40" r="78" fill="url(#sun)"/>
    <circle cx="392" cy="40" r="20" fill="#ffe3a3" fill-opacity="0.85"/>
    <g fill="#1c0826" fill-opacity="0.35" transform="translate(352 152) scale(1.15)">{ACACIA}</g>
    <path d="M0 200 C 120 190, 300 206, 440 194 L440 214 L0 214 Z" fill="#1c0826" fill-opacity="0.35"/>
    <text x="28" y="62" font-size="24" font-weight="800" fill="#ffffff">{escape(title)}</text>
    {desc_svg}
    {chip_svg}
  </g>
</svg>
'''
    (ASSETS / "projects" / f"{key}.svg").write_text(svg, encoding="utf-8")


def stack_panel():
    width, row_h, top = 900, 58, 74
    height = top + row_h * len(STACK) + 18
    rows = []
    for i, (label, items) in enumerate(STACK):
        y = top + i * row_h
        rows.append(f'<text x="34" y="{y + 18}" font-size="15" font-weight="700" fill="#ffd9c2">{escape(label)}</text>')
        chip_svg, _ = chips(items, 190, y, size=13.5, fill="#ffffff", fill_opacity=0.16)
        rows.append(chip_svg)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="Tech stack: {escape("; ".join(f"{label}: {', '.join(items)}" for label, items in STACK))}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#1e0b3b"/>
      <stop offset="0.55" stop-color="#5b1f6e"/>
      <stop offset="1" stop-color="#c2396d"/>
    </linearGradient>
    <clipPath id="c"><rect width="{width}" height="{height}" rx="20"/></clipPath>
  </defs>
  <g clip-path="url(#c)" font-family="{FONT}">
    <rect width="{width}" height="{height}" fill="url(#bg)"/>
    <circle cx="{width - 70}" cy="34" r="90" fill="#ff7a59" fill-opacity="0.18"/>
    <text x="34" y="46" font-size="22" font-weight="800" fill="#ffffff">Tools I build with</text>
    {"".join(rows)}
  </g>
</svg>
'''
    (ASSETS / "stack.svg").write_text(svg, encoding="utf-8")


def divider(name, label):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 60" width="900" height="60" role="img" aria-label="{escape(label)}">
  <defs>
    <linearGradient id="line" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#5b1f6e" stop-opacity="0"/>
      <stop offset="0.2" stop-color="#c2396d"/>
      <stop offset="0.5" stop-color="#ff7a59"/>
      <stop offset="0.8" stop-color="#c2396d"/>
      <stop offset="1" stop-color="#5b1f6e" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="txt" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#c2396d"/>
      <stop offset="1" stop-color="#ff7a59"/>
    </linearGradient>
  </defs>
  <path d="M0 44 C 150 30, 300 54, 450 40 S 750 30, 900 44" fill="none" stroke="url(#line)" stroke-width="3"/>
  <circle cx="450" cy="40" r="9" fill="#ffc07a"/>
  <text x="450" y="24" font-family="{FONT}" font-size="22" font-weight="800" fill="url(#txt)" text-anchor="middle">{escape(label)}</text>
</svg>
'''
    (ASSETS / f"{name}.svg").write_text(svg, encoding="utf-8")


def footer():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 120" width="900" height="120" role="img" aria-label="Asante for visiting!">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ff7a59"/>
      <stop offset="1" stop-color="#5b1f6e"/>
    </linearGradient>
    <clipPath id="c"><rect width="900" height="120" rx="20"/></clipPath>
  </defs>
  <g clip-path="url(#c)">
    <rect width="900" height="120" fill="url(#bg)"/>
    <circle cx="450" cy="120" r="54" fill="#ffd27a" fill-opacity="0.9"/>
    <path d="M0 100 C 150 86, 300 104, 450 94 S 750 86, 900 100 L900 120 L0 120 Z" fill="#1c0826"/>
    <g fill="#1c0826" transform="translate(110 64) scale(0.6)">{ACACIA}</g>
    <g fill="#1c0826" transform="translate(720 70) scale(0.5)">{ACACIA}</g>
    <text x="450" y="50" font-family="{FONT}" font-size="26" font-weight="800" fill="#ffffff" text-anchor="middle">Asante for visiting!</text>
  </g>
</svg>
'''
    (ASSETS / "footer.svg").write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    (ASSETS / "projects").mkdir(parents=True, exist_ok=True)
    for project in PROJECTS:
        project_card(*project)
    stack_panel()
    for name, label in [
        ("divider-about", "About me"),
        ("divider-projects", "Projects"),
        ("divider-stack", "Tech stack"),
        ("divider-stats", "GitHub activity"),
    ]:
        divider(name, label)
    footer()
    print("Generated", len(list(ASSETS.rglob("*.svg"))), "SVG files")

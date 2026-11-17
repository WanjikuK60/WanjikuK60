"""Generate the profile's SVG cards, tech-stack panel and dividers.

Run from the repo root:  python tools/make_assets.py
Edit PROJECTS or ABOUT below, re-run, and commit the changed SVGs.
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


W = 'fill="#ffffff"'
ACC = 'fill="#ffd27a"'
ART = {
    "az900": f'<path d="M20 44 a16 16 0 0 1 30 -8 a14 14 0 0 1 26 8 a12 12 0 0 1 -2 24 h-50 a12 12 0 0 1 -4 -24 z" {W} fill-opacity="0.92"/>'
             f'<path d="M14 82 q 18 -10 31 0 q 13 -10 31 0 v 26 q -18 -10 -31 0 q -13 -10 -31 0 z" {ACC}/>'
             f'<path d="M45 82 v 26" stroke="#5b1f6e" stroke-width="2"/>',
    "savannah": f'<ellipse cx="34" cy="46" rx="13" ry="30" {ACC}/>'
                f'<path d="M34 76 q -26 -6 -30 -34 q 18 8 30 22 q 12 -14 30 -22 q -4 28 -30 34 z" fill="#7fd18b"/>'
                f'<path d="M34 76 v 26" stroke="#7fd18b" stroke-width="4"/>'
                + "".join(f'<ellipse cx="72" cy="{104 - i * 8}" rx="14" ry="5" {ACC} stroke="#c2396d" stroke-width="1.5"/>' for i in range(4)),
    "kiroween": f'<circle cx="70" cy="18" r="13" {ACC}/>'
                f'<path d="M12 104 v -46 l 24 -24 l 24 24 v 46 z" fill="#1c0826"/>'
                f'<path d="M52 104 v -30 l 16 -14 l 16 14 v 30 z" fill="#1c0826"/>'
                f'<rect x="24" y="64" width="9" height="11" {ACC}/><rect x="40" y="64" width="9" height="11" {ACC}/>'
                f'<rect x="64" y="82" width="8" height="10" {ACC}/><path d="M30 104 v -16 a6 6 0 0 1 12 0 v 16 z" {ACC}/>'
                f'<path d="M6 30 q 6 -6 10 0 q 4 -6 10 0 q -4 2 -10 6 q -6 -4 -10 -6 z" fill="#1c0826"/>',
    "northstar": f'<path d="M44 6 L54 40 L88 50 L54 60 L44 94 L34 60 L0 50 L34 40 Z" {W} fill-opacity="0.92"/>'
                 f'<path d="M50 62 L38 84 H50 L42 108 L66 78 H54 L62 62 Z" {ACC}/>',
    "system-design": "".join(
                 f'<g transform="translate({x} {y})"><ellipse cx="14" cy="0" rx="14" ry="5" {ACC}/>'
                 f'<path d="M0 0 v 20 a14 5 0 0 0 28 0 v -20" {W} fill-opacity="0.9"/><ellipse cx="14" cy="0" rx="14" ry="5" {ACC}/></g>'
                 for x, y in [(30, 10), (4, 72), (56, 72)]) +
                 '<path d="M44 38 L18 70 M44 38 L70 70 M32 86 H56" stroke="#ffffff" stroke-width="2.5" stroke-dasharray="4 4"/>',
    "solstice": f'<circle cx="44" cy="40" r="22" {ACC}/>'
                + "".join(f'<rect x="42" y="2" width="4" height="10" rx="2" {ACC} transform="rotate({a} 44 40)"/>' for a in range(0, 360, 45)) +
                f'<path d="M8 74 h 72 v 10 a6 6 0 0 0 0 12 v 10 h -72 v -10 a6 6 0 0 0 0 -12 z" {W} fill-opacity="0.92"/>'
                f'<path d="M30 76 v 28" stroke="#c2396d" stroke-width="2" stroke-dasharray="3 3"/>',
    "quicknotes": f'<rect x="10" y="12" width="56" height="84" rx="6" {W} fill-opacity="0.92"/>'
                  f'<rect x="10" y="12" width="56" height="12" rx="6" {ACC}/>'
                  + "".join(f'<rect x="18" y="{34 + i * 12}" width="{40 - (i % 2) * 12}" height="4" rx="2" fill="#c2396d" fill-opacity="0.7"/>' for i in range(5)) +
                  f'<g transform="rotate(35 72 70)"><rect x="66" y="30" width="12" height="62" rx="3" {ACC}/><path d="M66 92 h12 l-6 12 z" fill="#1c0826"/></g>',
    "chat-cartographer": f'<path d="M8 14 h 58 a8 8 0 0 1 8 8 v 30 a8 8 0 0 1 -8 8 h -34 l -14 12 v -12 h -10 a8 8 0 0 1 -8 -8 v -30 a8 8 0 0 1 8 -8 z" {W} fill-opacity="0.92"/>'
                         + "".join(f'<circle cx="{24 + i * 14}" cy="37" r="4" fill="#7a2d8a"/>' for i in range(3)) +
                         f'<path d="M66 66 a16 16 0 0 1 16 16 c 0 12 -16 28 -16 28 s -16 -16 -16 -28 a16 16 0 0 1 16 -16 z" {ACC}/>'
                         f'<circle cx="66" cy="82" r="6" fill="#2a0f36"/>',
}

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
    lines = textwrap.wrap(desc, 37)[:3]
    desc_svg = "".join(
        f'<text x="28" y="{96 + i * 22}" font-size="15.5" fill="#ffffff" fill-opacity="0.92">{escape(line)}</text>'
        for i, line in enumerate(lines)
    )
    chip_svg, _ = chips(tags, 28, 174)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 224" width="440" height="224" role="img" aria-label="{escape(title)}: {escape(desc)}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{start}"/>
      <stop offset="1" stop-color="{end}"/>
    </linearGradient>
    <linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#ffffff" stop-opacity="0.28"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="c"><rect width="440" height="224" rx="18"/></clipPath>
    <style>
      .sweep {{ animation: sweep 6s ease-in-out infinite; }}
      @keyframes sweep {{ 0%, 55% {{ transform: translateX(-260px) skewX(-20deg); }} 85%, 100% {{ transform: translateX(560px) skewX(-20deg); }} }}
      .float {{ animation: float 4s ease-in-out infinite alternate; }}
      @keyframes float {{ from {{ transform: translateY(0); }} to {{ transform: translateY(-6px); }} }}
      .dot {{ animation: pulse 1.6s ease-in-out infinite; }}
      @keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: .3; }} }}
      @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
    </style>
  </defs>
  <g clip-path="url(#c)" font-family="{FONT}">
    <rect width="440" height="224" fill="url(#bg)"/>
    <circle cx="400" cy="200" r="120" fill="#ffffff" fill-opacity="0.06"/>
    <circle cx="380" cy="150" r="58" fill="#ffd27a" fill-opacity="0.12"/>
    <path d="M0 208 C 120 198, 300 214, 440 202 L440 224 L0 224 Z" fill="#1c0826" fill-opacity="0.3"/>
    <g class="float"><g transform="translate(336 76)">{ART[key]}</g></g>
    <rect x="356" y="18" width="66" height="24" rx="12" fill="#1c0826" fill-opacity="0.35"/>
    <circle class="dot" cx="370" cy="30" r="4" fill="#7fe0a0"/>
    <text x="380" y="35" font-size="12" font-weight="800" fill="#ffffff" letter-spacing="1">LIVE</text>
    <text x="28" y="56" font-size="24" font-weight="800" fill="#ffffff">{escape(title)}</text>
    {desc_svg}
    {chip_svg}
    <rect class="sweep" x="0" y="-20" width="120" height="270" fill="url(#sweep)"/>
  </g>
</svg>
'''
    (ASSETS / "projects" / f"{key}.svg").write_text(svg, encoding="utf-8")


def divider(name, label):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 70" width="900" height="70" role="img" aria-label="{escape(label)}">
  <defs>
    <linearGradient id="line" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#5b1f6e" stop-opacity="0"/>
      <stop offset="0.25" stop-color="#c2396d"/>
      <stop offset="0.5" stop-color="#ff7a59"/>
      <stop offset="0.75" stop-color="#c2396d"/>
      <stop offset="1" stop-color="#5b1f6e" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="txt" gradientUnits="userSpaceOnUse" x1="300" y1="0" x2="600" y2="0">
      <stop offset="0" stop-color="#c2396d"/>
      <stop offset="0.45" stop-color="#ff7a59"/>
      <stop offset="0.5" stop-color="#ffc07a"/>
      <stop offset="0.55" stop-color="#ff7a59"/>
      <stop offset="1" stop-color="#c2396d"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="-300 0;300 0" dur="4s" repeatCount="indefinite"/>
    </linearGradient>
    <radialGradient id="sun" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ffd27a"/>
      <stop offset="1" stop-color="#ffd27a" stop-opacity="0"/>
    </radialGradient>
    <style>
      .bob {{ animation: bob 3s ease-in-out infinite alternate; }}
      @keyframes bob {{ from {{ transform: translateY(0); }} to {{ transform: translateY(-4px); }} }}
      @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
    </style>
  </defs>
  <path d="M0 56 C 150 42, 300 66, 450 52 S 750 42, 900 56" fill="none" stroke="url(#line)" stroke-width="3"/>
  <g class="bob"><circle cx="450" cy="52" r="18" fill="url(#sun)"/><circle cx="450" cy="52" r="8" fill="#ffc07a"/></g>
  <text x="450" y="30" font-family="{FONT}" font-size="26" font-weight="900" fill="url(#txt)" text-anchor="middle" letter-spacing="1">{escape(label)}</text>
</svg>
'''
    (ASSETS / f"{name}.svg").write_text(svg, encoding="utf-8")



ABOUT = [
    ("Learning", ["Software Engineering student", "at Power Learn Project", "1MillionDevs"], "#c2396d", "cap"),
    ("Home", ["Nairobi, Kenya", "I speak English", "and Kiswahili"], "#ff7a59", "pin"),
    ("Growing in", ["Azure (AZ-900),", "system design and", "fair, human-centred AI"], "#8c2f6a", "leaf"),
]
ICONS = {
    "cap": '<path d="M0 -10 L22 0 L0 10 L-22 0 Z" fill="#fff"/><path d="M-12 5 v8 q12 8 24 0 v-8" fill="#fff" fill-opacity="0.85"/><path d="M18 2 v12" stroke="#ffd27a" stroke-width="3"/>',
    "pin": '<path d="M0 18 c0 0 -16 -14 -16 -26 a16 16 0 0 1 32 0 c0 12 -16 26 -16 26 z" fill="#fff"/><circle cx="0" cy="-8" r="6" fill="#ffd27a"/>',
    "leaf": '<path d="M0 18 v-16" stroke="#fff" stroke-width="3"/><path d="M0 4 c-18 0 -20 -16 -20 -20 c14 0 20 8 20 20 z" fill="#fff"/><path d="M0 0 c14 0 18 -12 18 -16 c-12 0 -18 6 -18 16 z" fill="#ffd27a"/>',
}


def about_card():
    width, height = 900, 236
    tiles = []
    for i, (label, lines, color, icon) in enumerate(ABOUT):
        x, y = 24 + i * 288, 24
        text = "".join(
            f'<text x="{x + 138}" y="{y + 128 + j * 24}" font-size="16" fill="#ffffff" text-anchor="middle"'
            f'{" font-weight=\"700\"" if j == len(lines) - 1 else ""}>{escape(line)}</text>'
            for j, line in enumerate(lines)
        )
        tiles.append(f'''<g class="tile" style="animation-delay: {0.18 * i:.2f}s">
      <rect x="{x}" y="{y}" width="276" height="188" rx="18" fill="#ffffff" fill-opacity="0.08" stroke="#ffffff" stroke-opacity="0.18"/>
      <circle cx="{x + 138}" cy="{y + 50}" r="30" fill="{color}"/>
      <g transform="translate({x + 138} {y + 52}) scale(0.85)">{ICONS[icon]}</g>
      <text x="{x + 138}" y="{y + 102}" font-size="13" font-weight="800" fill="#ffd27a" letter-spacing="2" text-anchor="middle">{escape(label.upper())}</text>
      {text}
    </g>''')
    summary = " ".join(f"{label}: {' '.join(lines)}." for label, lines, _, _ in ABOUT)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="About me. {escape(summary)}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1e0b3b"/>
      <stop offset="0.55" stop-color="#4a1860"/>
      <stop offset="1" stop-color="#9a2f68"/>
    </linearGradient>
    <clipPath id="c"><rect width="{width}" height="{height}" rx="22"/></clipPath>
    <style>
      .tile {{ animation: pop .9s cubic-bezier(.2,.8,.2,1) both; }}
      @keyframes pop {{ from {{ opacity: 0; transform: translateY(14px); }} to {{ opacity: 1; transform: translateY(0); }} }}
      @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
    </style>
  </defs>
  <g clip-path="url(#c)" font-family="{FONT}">
    <rect width="{width}" height="{height}" fill="url(#bg)"/>
    <circle cx="{width - 40}" cy="30" r="130" fill="#ff7a59" fill-opacity="0.16"/>
    <circle cx="40" cy="{height}" r="110" fill="#c2396d" fill-opacity="0.2"/>
    {"".join(tiles)}
  </g>
</svg>
'''
    (ASSETS / "about.svg").write_text(svg, encoding="utf-8")


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
    for name, label in [
        ("divider-about", "About me"),
        ("divider-projects", "Projects"),
        ("divider-stack", "Tech stack"),
        ("divider-stats", "GitHub activity"),
    ]:
        divider(name, label)
    footer()
    about_card()
    print("Generated", len(list(ASSETS.rglob("*.svg"))), "SVG files")

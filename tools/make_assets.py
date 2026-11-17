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



MONO = "'Cascadia Code', 'Fira Code', Consolas, 'Courier New', monospace"

# (text, colour) spans per line of the About-me "code window"
K, N, S, P, D, F = "#ff8fb8", "#ffd27a", "#ffc07a", "#efe3ff", "#c9a8dc", "#7fe0c4"
CODE = [
    [("class ", K), ("Wanjiku", N), ("(", P), ("SoftwareEngineer", F), ("):", P)],
    [('    """A girl in the Tech World.', D)],
    [('    A Software Engineer in the making."""', D)],
    [],
    [("    home ", P), ("= ", K), ('"Nairobi, Kenya"', S)],
    [("    speaks ", P), ("= ", K), ("[", P), ('"English"', S), (", ", P), ('"Kiswahili"', S), ("]", P)],
    [("    codes_in ", P), ("= ", K), ("[", P), ('"Python"', S), (", ", P), ('"JavaScript"', S), (", ", P), ('"TypeScript"', S), ("]", P)],
    [("    learning ", P), ("= ", K), ("[", P), ('"Azure"', S), (", ", P), ('"System design"', S), (", ", P), ('"Fair AI"', S), ("]", P)],
    [("    programme ", P), ("= ", K), ('"PLP 1MillionDevs"', S)],
    [],
    [("    def ", K), ("mission", F), ("(self):", P)],
    [("        return ", K), ('"Build tech that works for Africa"', S)],
    [],
    [("# Karibu! Let's build something together", D)],
]

FACTS = [
    ("🦒", "My study buddy explains", "the cloud in Kiswahili", "and Sheng", "#ffd27a"),
    ("👻", "I turned my portfolio", "into a haunted mansion", "for a hackathon", "#ff9ac1"),
    ("🌽", "I taught a loan model", "to follow harvest seasons,", "not payslips", "#ffb27a"),
    ("⚡", "I shipped a working", "webhook on Day 1", "of an industry sprint", "#c8a6ff"),
]


def about_card():
    width, height = 900, 452
    code_lines = []
    for i, spans in enumerate(CODE):
        y = 90 + i * 24.5
        tspans = "".join(f'<tspan fill="{color}">{escape(text)}</tspan>' for text, color in spans)
        code_lines.append(
            f'<text class="line" style="animation-delay: {0.35 + i * 0.22:.2f}s" x="58" y="{y}" xml:space="preserve">{tspans}</text>'
            f'<text x="34" y="{y}" fill="#7d5a92" font-size="13" text-anchor="end">{i + 1}</text>'
        )
    cursor_y = 90 + (len(CODE) - 1) * 24.5
    cursor_x = 58 + len("".join(text for text, _ in CODE[-1])) * 8.7 + 4
    notes = []
    for i, (emoji, l1, l2, l3, color) in enumerate(FACTS):
        y = 70 + i * 92
        tilt = (-2, 1.6, -1.2, 2)[i]
        notes.append(f'''<g class="note n{i}" style="transform-origin: 728px {y + 40}px; --tilt: {tilt}deg">
      <rect x="580" y="{y}" width="296" height="80" rx="12" fill="{color}"/>
      <rect x="700" y="{y - 6}" width="56" height="14" rx="3" fill="#ffffff" fill-opacity="0.55"/>
      <text x="604" y="{y + 50}" font-size="30">{emoji}</text>
      <text x="650" y="{y + 26}" font-size="14.5" font-weight="600" fill="#2a0f36">{escape(l1)}</text>
      <text x="650" y="{y + 46}" font-size="14.5" font-weight="600" fill="#2a0f36">{escape(l2)}</text>
      <text x="650" y="{y + 66}" font-size="14.5" font-weight="800" fill="#2a0f36">{escape(l3)}</text>
    </g>''')
    summary = ("A girl in the Tech World. A Software Engineer in the making. Home: Nairobi, Kenya. "
               "Speaks English and Kiswahili. Codes in Python, JavaScript and TypeScript. Learning Azure, "
               "system design and fair AI, in the PLP 1MillionDevs programme. Mission: build tech that works for Africa. "
               "Fun facts: " + " ".join(f"{a} {b} {c}." for _, a, b, c, _ in FACTS))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="About me. {escape(summary)}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1e0b3b"/>
      <stop offset="0.55" stop-color="#4a1860"/>
      <stop offset="1" stop-color="#b13468"/>
    </linearGradient>
    <linearGradient id="bar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#c2396d"/>
      <stop offset="1" stop-color="#ff7a59"/>
    </linearGradient>
    <clipPath id="c"><rect width="{width}" height="{height}" rx="22"/></clipPath>
    <style>
      .line {{ opacity: 0; animation: typein .5s steps(12, end) forwards; }}
      @keyframes typein {{ from {{ opacity: 0; clip-path: inset(0 100% 0 0); }} to {{ opacity: 1; clip-path: inset(0 0 0 0); }} }}
      .cursor {{ animation: blink .9s steps(1) infinite; }}
      @keyframes blink {{ 50% {{ opacity: 0; }} }}
      .note {{ transform: rotate(var(--tilt)); animation: wobble 4s ease-in-out infinite alternate; }}
      .n1 {{ animation-delay: -1s; }} .n2 {{ animation-delay: -2s; }} .n3 {{ animation-delay: -3s; }}
      @keyframes wobble {{ from {{ transform: rotate(var(--tilt)) translateY(0); }} to {{ transform: rotate(calc(var(--tilt) * -1)) translateY(-4px); }} }}
      @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} .line {{ opacity: 1; }} }}
    </style>
  </defs>
  <g clip-path="url(#c)" font-family="{FONT}">
    <rect width="{width}" height="{height}" fill="url(#bg)"/>
    <circle cx="{width - 30}" cy="20" r="140" fill="#ff7a59" fill-opacity="0.14"/>
    <circle cx="20" cy="{height}" r="120" fill="#c2396d" fill-opacity="0.18"/>

    <!-- Code window -->
    <rect x="18" y="20" width="540" height="{height - 40}" rx="16" fill="#140724" fill-opacity="0.92" stroke="#ffffff" stroke-opacity="0.12"/>
    <path d="M18 36 a16 16 0 0 1 16 -16 h508 a16 16 0 0 1 16 16 v18 h-540 z" fill="url(#bar)"/>
    <circle cx="40" cy="38" r="6" fill="#ff5f57"/><circle cx="60" cy="38" r="6" fill="#febc2e"/><circle cx="80" cy="38" r="6" fill="#28c840"/>
    <text x="288" y="43" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">about_me.py</text>
    <g font-family="{MONO}" font-size="14.5">
      {"".join(code_lines)}
    </g>
    <rect class="cursor" x="{cursor_x:.0f}" y="{cursor_y - 15}" width="9" height="19" fill="#ffd27a"/>

    <!-- Fun facts -->
    <text x="728" y="46" font-size="20" font-weight="900" fill="#ffd27a" text-anchor="middle" letter-spacing="1">✨ Fun facts ✨</text>
    {"".join(notes)}
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

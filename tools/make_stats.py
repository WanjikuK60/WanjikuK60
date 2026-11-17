"""Draw sunset-themed GitHub stats and top-languages cards.

Runs daily in .github/workflows/snake.yml with the workflow's GITHUB_TOKEN and
writes dist/stats.svg and dist/languages.svg, which the README shows.

Locally:  GITHUB_TOKEN=... python tools/make_stats.py WanjikuK60 dist
          python tools/make_stats.py --sample dist   (no network, fake numbers)
"""

import json
import os
import sys
import urllib.request
from html import escape
from pathlib import Path

FONT = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
PALETTE = ["#ffd27a", "#ffb26b", "#ff7a59", "#e8517a", "#c2396d", "#8c2f6a"]

QUERY = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    pullRequests { totalCount }
    repositories(ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC, first: 100) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name } }
        }
      }
    }
    contributionsCollection {
      totalCommitContributions
      contributionCalendar { totalContributions }
    }
  }
}
"""


def fetch(login: str, token: str) -> dict:
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    if "errors" in payload:
        raise SystemExit(f"GitHub API error: {payload['errors']}")
    user = payload["data"]["user"]
    repos = user["repositories"]
    sizes: dict[str, int] = {}
    for repo in repos["nodes"]:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            sizes[name] = sizes.get(name, 0) + edge["size"]
    return {
        "contributions": user["contributionsCollection"]["contributionCalendar"]["totalContributions"],
        "commits": user["contributionsCollection"]["totalCommitContributions"],
        "prs": user["pullRequests"]["totalCount"],
        "repos": repos["totalCount"],
        "stars": sum(r["stargazerCount"] for r in repos["nodes"]),
        "followers": user["followers"]["totalCount"],
        "languages": sizes,
    }


def sample() -> dict:
    return {
        "contributions": 412, "commits": 356, "prs": 64, "repos": 11, "stars": 3, "followers": 5,
        "languages": {"TypeScript": 420000, "JavaScript": 260000, "Python": 150000,
                      "CSS": 90000, "HTML": 60000, "Shell": 4000},
    }


def background(width: int, height: int) -> str:
    return f'''<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1e0b3b"/>
      <stop offset="0.6" stop-color="#5b1f6e"/>
      <stop offset="1" stop-color="#c2396d"/>
    </linearGradient>
    <clipPath id="c"><rect width="{width}" height="{height}" rx="18"/></clipPath>
  </defs>
  <g clip-path="url(#c)">
    <rect width="{width}" height="{height}" fill="url(#bg)"/>
    <circle cx="{width - 46}" cy="40" r="60" fill="#ff7a59" fill-opacity="0.22"/>
    <circle cx="{width - 46}" cy="40" r="16" fill="#ffd27a" fill-opacity="0.9"/>
  </g>'''


def stats_svg(s: dict) -> str:
    rows = [
        ("Contributions in the last year", s["contributions"]),
        ("Commits in the last year", s["commits"]),
        ("Pull requests", s["prs"]),
        ("Public repositories", s["repos"]),
        ("Stars earned", s["stars"]),
    ]
    width, height = 440, 212
    body = []
    for i, (label, value) in enumerate(rows):
        y = 74 + i * 27
        body.append(
            f'<circle cx="30" cy="{y - 5}" r="5" fill="{PALETTE[i]}"/>'
            f'<text x="46" y="{y}" font-size="15" fill="#ffe9dc">{escape(label)}</text>'
            f'<text x="{width - 28}" y="{y}" font-size="16" font-weight="800" fill="#ffffff" text-anchor="end">{value:,}</text>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="GitHub stats: {", ".join(f"{label} {value}" for label, value in rows)}">
  {background(width, height)}
  <g font-family="{FONT}">
    <text x="24" y="38" font-size="20" font-weight="800" fill="#ffd27a">My GitHub activity</text>
    {"".join(body)}
  </g>
</svg>
'''


def languages_svg(s: dict) -> str:
    total = sum(s["languages"].values()) or 1
    top = sorted(s["languages"].items(), key=lambda kv: kv[1], reverse=True)[:6]
    width, height = 440, 212
    bar_x, bar_w, bar_y = 24, width - 48, 58
    parts, x = [], bar_x
    for i, (_, size) in enumerate(top):
        w = bar_w * size / total
        parts.append(f'<rect x="{x:.1f}" y="{bar_y}" width="{max(w, 2):.1f}" height="14" fill="{PALETTE[i]}"/>')
        x += w
    legend = []
    for i, (name, size) in enumerate(top):
        col, row = i % 2, i // 2
        lx, ly = 30 + col * 200, 112 + row * 30
        legend.append(
            f'<circle cx="{lx}" cy="{ly - 5}" r="6" fill="{PALETTE[i]}"/>'
            f'<text x="{lx + 14}" y="{ly}" font-size="15" fill="#ffffff">{escape(name)}</text>'
            f'<text x="{lx + 170}" y="{ly}" font-size="14" fill="#ffd9c2" text-anchor="end">{100 * size / total:.1f}%</text>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="Most used languages: {", ".join(f"{n} {100 * v / total:.1f}%" for n, v in top)}">
  {background(width, height)}
  <g font-family="{FONT}">
    <text x="24" y="38" font-size="20" font-weight="800" fill="#ffd27a">Most used languages</text>
    <clipPath id="bar"><rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="14" rx="7"/></clipPath>
    <g clip-path="url(#bar)">{"".join(parts)}</g>
    {"".join(legend)}
  </g>
</svg>
'''


def main(argv: list[str]) -> None:
    if argv[:1] == ["--sample"]:
        data, out = sample(), Path(argv[1])
    else:
        login, out = argv[0], Path(argv[1])
        data = fetch(login, os.environ["GITHUB_TOKEN"])
    out.mkdir(parents=True, exist_ok=True)
    (out / "stats.svg").write_text(stats_svg(data), encoding="utf-8")
    (out / "languages.svg").write_text(languages_svg(data), encoding="utf-8")
    print(f"Wrote stats for {data['repos']} repos to {out}")


if __name__ == "__main__":
    main(sys.argv[1:])

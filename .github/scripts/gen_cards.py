#!/usr/bin/env python3
"""Render the animated SVG cards used by the profile README.

The popular hosted card services (github-readme-stats and friends) render as
broken images the moment their shared deployment is paused or rate-limited --
which is exactly what happened while this profile was being built. Generating
the cards here instead means the profile depends on nothing but the GitHub API
and this file.

Every card is a self-contained SVG with declarative CSS/SMIL animation. That is
the only kind of animation GitHub will render: it strips <script> from README
HTML, and it strips it from SVGs too, but animation defined in <style> or via
<animate> inside an SVG referenced by <img> plays normally.

Usage:
    GITHUB_TOKEN=... python .github/scripts/gen_cards.py [--out assets]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

API = "https://api.github.com/graphql"

# --- Palette -----------------------------------------------------------------
# Built around Go's brand cyan, which is also this profile's accent colour.
BG = "#0d1117"
CARD = "#0d1117"
BORDER = "#1f2733"
ACCENT = "#00ADD8"
TEXT = "#e6edf3"
MUTED = "#8b949e"
FONT = "'Segoe UI',Ubuntu,'Helvetica Neue',Arial,sans-serif"
MONO = "'SFMono-Regular',Consolas,'Liberation Mono',monospace"

# Cyan ramp for the contribution heatmap, darkest (no contributions) first.
HEAT = ["#161b22", "#0a3a47", "#10697f", "#0f9dbd", "#56dcf7"]

QUERY = """
query($login: String!) {
  user(login: $login) {
    login
    repositories(ownerAffiliations: OWNER, privacy: PUBLIC, isFork: false, first: 100) {
      totalCount
      nodes {
        name
        languages(first: 12, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
    contributionsCollection {
      totalCommitContributions
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays { contributionCount date weekday }
        }
      }
    }
  }
}
"""


def esc(text: str) -> str:
    """Escape text for inclusion in XML character data or an attribute value."""
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def fetch(login: str, token: str) -> dict:
    body = json.dumps({"query": QUERY, "variables": {"login": login}}).encode()
    request = urllib.request.Request(
        API,
        data=body,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": f"{login}-profile-cards",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read())
    except urllib.error.HTTPError as exc:  # pragma: no cover - network path
        sys.exit(f"GitHub API returned HTTP {exc.code}: {exc.read()[:400]!r}")

    # A GraphQL error arrives with HTTP 200, so it has to be checked explicitly
    # rather than left to raise_for_status-style handling.
    if payload.get("errors"):
        sys.exit(f"GraphQL errors: {json.dumps(payload['errors'])[:500]}")
    if not payload.get("data", {}).get("user"):
        sys.exit(f"No such user: {login}")
    return payload["data"]["user"]


def languages(user: dict) -> list[tuple[str, int, str]]:
    """Aggregate language byte counts across every public, non-fork repository."""
    totals: dict[str, list] = {}
    for repo in user["repositories"]["nodes"]:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            entry = totals.setdefault(name, [0, edge["node"]["color"] or MUTED])
            entry[0] += edge["size"]
    ranked = sorted(totals.items(), key=lambda kv: -kv[1][0])
    return [(name, size, colour) for name, (size, colour) in ranked]


def human_bytes(value: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if value < 1024 or unit == "GB":
            return f"{value:.0f} {unit}" if unit == "B" else f"{value:.1f} {unit}"
        value /= 1024.0
    return f"{value:.1f} GB"


# --- Cards -------------------------------------------------------------------

def card_open(width: int, height: int, title: str, extra_css: str = "") -> list[str]:
    """Common card chrome: rounded panel, border, animated title."""
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{esc(title)}" '
        'font-size="13">',
        "<style>",
        f"  .t{{font:600 15px {FONT};fill:{TEXT}}}",
        f"  .l{{font:400 12px {FONT};fill:{MUTED}}}",
        f"  .v{{font:600 12px {MONO};fill:{TEXT}}}",
        "  .fade{opacity:0;animation:fade .6s ease-out forwards}",
        "  @keyframes fade{from{opacity:0;transform:translateY(6px)}"
        "to{opacity:1;transform:translateY(0)}}",
        "  @media(prefers-reduced-motion:reduce){",
        "    .fade,.cell{animation:none!important;opacity:1!important}",
        "  }",
        extra_css,
        "</style>",
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="8" '
        f'fill="{CARD}" stroke="{BORDER}"/>',
        # A short accent rule that draws itself in, under the card title.
        f'<rect x="20" y="41" height="2" rx="1" fill="{ACCENT}" width="0">'
        f'<animate attributeName="width" from="0" to="34" dur="0.7s" '
        f'begin="0.1s" fill="freeze"/></rect>',
        f'<text x="20" y="32" class="t fade" style="animation-delay:0s">'
        f"{esc(title)}</text>",
    ]


def render_languages(user: dict, out: Path) -> None:
    """Stacked proportion bar plus an animated legend of the top languages."""
    ranked = languages(user)
    total = sum(size for _, size, _ in ranked) or 1
    top = ranked[:6]
    shown = sum(size for _, size, _ in top)
    rows = [(n, s, c) for n, s, c in top]
    if shown < total:
        rows.append(("Other", total - shown, "#6e7681"))

    width, height = 420, 300
    bar_x, bar_y, bar_w, bar_h = 20, 62, width - 40, 12
    svg = card_open(width, height, "Language distribution")

    # Stacked bar. Each segment grows from zero, left to right, so the bar
    # assembles itself rather than simply appearing.
    svg.append(f'<clipPath id="barclip"><rect x="{bar_x}" y="{bar_y}" '
               f'width="{bar_w}" height="{bar_h}" rx="6"/></clipPath>')
    svg.append(f'<rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" '
               f'rx="6" fill="#161b22"/>')
    svg.append('<g clip-path="url(#barclip)">')
    offset = 0.0
    for index, (name, size, colour) in enumerate(rows):
        seg = bar_w * size / total
        svg.append(
            f'<rect x="{bar_x + offset:.2f}" y="{bar_y}" height="{bar_h}" '
            f'width="0" fill="{esc(colour)}">'
            f'<animate attributeName="width" from="0" to="{seg:.2f}" '
            f'dur="0.8s" begin="{0.15 + index * 0.09:.2f}s" fill="freeze"/></rect>'
        )
        offset += seg
    svg.append("</g>")

    # Legend: two columns, each row fading in on a stagger.
    top_y = bar_y + bar_h + 30
    for index, (name, size, colour) in enumerate(rows):
        col, row = index % 2, index // 2
        x = 20 + col * (bar_w // 2)
        y = top_y + row * 34
        delay = 0.35 + index * 0.07
        svg.append(f'<g class="fade" style="animation-delay:{delay:.2f}s">')
        svg.append(f'<circle cx="{x + 5}" cy="{y - 4}" r="5" fill="{esc(colour)}"/>')
        svg.append(f'<text x="{x + 17}" y="{y}" class="l" '
                   f'fill="{TEXT}">{esc(name)}</text>')
        svg.append(f'<text x="{x + 17}" y="{y + 15}" class="v" '
                   f'fill="{MUTED}">{100 * size / total:.1f}%</text>')
        svg.append("</g>")

    svg.append(
        f'<text x="20" y="{height - 16}" class="l fade" '
        f'style="animation-delay:0.9s">{esc(human_bytes(total))} across '
        f'{user["repositories"]["totalCount"]} public repositories</text>'
    )
    svg.append("</svg>")
    (out / "langs.svg").write_text("\n".join(svg), encoding="utf-8")


def render_stats(user: dict, out: Path) -> None:
    """A row of headline figures, each sliding in on a stagger."""
    ranked = languages(user)
    # Deliberately no commit-count or streak tile. Those measure cadence rather
    # than output, and a burst-shaped commit history reads as inactivity even
    # when the shipped work is substantial. These four measure what was built.
    tiles = [
        (str(user["repositories"]["totalCount"]), "Public repos"),
        (human_bytes(sum(s for _, s, _ in ranked)), "Public code"),
        (str(len(ranked)), "Languages"),
        (ranked[0][0] if ranked else "--", "Primary language"),
    ]

    width, height = 420, 128
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="Profile statistics">',
        "<style>",
        f"  .n{{font:700 26px {FONT};fill:{ACCENT}}}",
        f"  .k{{font:400 11px {FONT};fill:{MUTED}}}",
        "  .fade{opacity:0;animation:fade .7s cubic-bezier(.2,.8,.2,1) forwards}",
        "  @keyframes fade{from{opacity:0;transform:translateY(10px)}"
        "to{opacity:1;transform:translateY(0)}}",
        "  @media(prefers-reduced-motion:reduce){"
        ".fade{animation:none!important;opacity:1!important}}",
        "</style>",
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="8" '
        f'fill="{CARD}" stroke="{BORDER}"/>',
    ]
    for index, (value, label) in enumerate(tiles):
        cx = (width / 4) * index + width / 8
        svg.append(f'<g class="fade" style="animation-delay:{index * 0.11:.2f}s">')
        svg.append(f'<text x="{cx:.1f}" y="62" class="n" '
                   f'text-anchor="middle">{esc(value)}</text>')
        svg.append(f'<text x="{cx:.1f}" y="84" class="k" '
                   f'text-anchor="middle">{esc(label)}</text>')
        svg.append("</g>")
    # Accent rule that sweeps the full width once the tiles have landed.
    svg.append(f'<rect x="20" y="104" height="2" rx="1" fill="{ACCENT}" '
               f'opacity="0.55" width="0"><animate attributeName="width" from="0" '
               f'to="{width - 40}" dur="1s" begin="0.4s" fill="freeze"/></rect>')
    svg.append("</svg>")
    (out / "stats.svg").write_text("\n".join(svg), encoding="utf-8")


def render_activity(user: dict, out: Path) -> None:
    """Contribution heatmap. Cells pop in column by column, left to right.

    Generated but deliberately not embedded in the README yet. The calendar
    currently reports contributions on 19 days of the year, so the card reads as
    a mostly-empty grid -- which undersells work that largely lives in private
    repositories. Turning on Settings -> Public profile -> "Include private
    contributions on my profile" is what makes this card worth showing; once it
    is on, uncomment the block in README.md.
    """
    calendar = user["contributionsCollection"]["contributionCalendar"]
    weeks = calendar["weeks"]
    counts = [d["contributionCount"] for w in weeks for d in w["contributionDays"]]
    peak = max(counts) if counts else 0

    def level(count: int) -> int:
        if count <= 0 or peak <= 0:
            return 0
        # Quartiles of the busiest day, so the ramp adapts to the account.
        for index, cut in enumerate((0.25, 0.5, 0.75), start=1):
            if count <= peak * cut:
                return index
        return 4

    cell, gap = 12, 3
    pitch = cell + gap
    left, top = 34, 66
    width = left + len(weeks) * pitch + 16
    height = top + 7 * pitch + 34

    stagger = 14  # ms between adjacent columns
    css = [
        "  .cell{opacity:0;animation:pop .45s ease-out forwards;"
        "transform-box:fill-box;transform-origin:center}",
        "  @keyframes pop{from{opacity:0;transform:scale(.35)}"
        "to{opacity:1;transform:scale(1)}}",
    ]
    # One delay class per column keeps the file small; 371 inline styles would
    # roughly triple it for no visible benefit.
    css += [
        f"  .w{index}{{animation-delay:{index * stagger}ms}}"
        for index in range(len(weeks))
    ]

    svg = card_open(width, height, "Contribution activity", "\n".join(css))

    for index, week in enumerate(weeks):
        x = left + index * pitch
        for day in week["contributionDays"]:
            y = top + day["weekday"] * pitch
            svg.append(
                f'<rect class="cell w{index}" x="{x}" y="{y}" width="{cell}" '
                f'height="{cell}" rx="3" fill="{HEAT[level(day["contributionCount"])]}">'
                f'<title>{day["contributionCount"]} on {day["date"]}</title></rect>'
            )

    # Month labels, written once per month at the column where it begins.
    seen = None
    for index, week in enumerate(weeks):
        days = week["contributionDays"]
        if not days:
            continue
        month = date.fromisoformat(days[0]["date"]).strftime("%b")
        if month != seen:
            seen = month
            svg.append(f'<text x="{left + index * pitch}" y="{top - 8}" '
                       f'class="l">{month}</text>')

    for row, label in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        svg.append(f'<text x="0" y="{top + row * pitch + cell - 2}" '
                   f'class="l" font-size="10">{label}</text>')

    # Legend.
    legend_x = width - 16 - 5 * pitch - 78
    baseline = height - 14
    svg.append(f'<text x="20" y="{baseline}" class="l">'
               f'{calendar["totalContributions"]:,} contributions in the last year'
               f"</text>")
    svg.append(f'<text x="{legend_x}" y="{baseline}" class="l" '
               f'font-size="10">Less</text>')
    for index, colour in enumerate(HEAT):
        svg.append(f'<rect x="{legend_x + 32 + index * pitch}" '
                   f'y="{baseline - 9}" width="{cell}" height="{cell}" rx="3" '
                   f'fill="{colour}"/>')
    svg.append(f'<text x="{legend_x + 32 + 5 * pitch + 4}" y="{baseline}" '
               f'class="l" font-size="10">More</text>')
    svg.append("</svg>")
    (out / "activity.svg").write_text("\n".join(svg), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--user", default=os.environ.get("PROFILE_USER", "victorakor"))
    parser.add_argument("--out", default="assets", type=Path)
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        return int(bool(sys.stderr.write("GITHUB_TOKEN is not set\n"))) or 1

    user = fetch(args.user, token)
    args.out.mkdir(parents=True, exist_ok=True)
    render_languages(user, args.out)
    render_stats(user, args.out)
    render_activity(user, args.out)
    print(f"wrote langs.svg, stats.svg, activity.svg to {args.out}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

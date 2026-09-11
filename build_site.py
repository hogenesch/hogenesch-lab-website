#!/usr/bin/env python3
"""Render alumni, HTML pages, and sitemap for the static lab site."""

from datetime import datetime
from html import escape
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
PAGES = [
    "index", "research", "people", "lineage", "collaborations",
    "publications", "press", "resources", "join",
]
OUTPUT_PAGES = PAGES + ["404"]


def alumni_entry(entry):
    name = escape(entry["name"])
    icon = ""
    if entry.get("icon"):
        icon = (
            f' <img class="inline-icon" src="{escape(entry["icon"])}" '
            f'alt="{escape(entry.get("icon_alt", ""))}" />'
        )
    role = escape(entry.get("role", ""))
    headline = f"<strong>{name}{icon}</strong>"
    if role:
        headline += f'<span class="alumni-role">{role}</span>'
    parts = [f'<li><div class="alumni-headline">{headline}</div>']
    if entry.get("current_institution"):
        parts.append(f'<span class="alumni-meta">{escape(entry["current_institution"])}</span>')
    if entry.get("current_position"):
        parts.append(f'<span class="alumni-current-line">{escape(entry["current_position"])}</span>')
    if entry.get("honor"):
        parts.append(f'<span class="alumni-honor">{escape(entry["honor"])}</span>')
    links = []
    for key, label in (("website", "Website"), ("scholar", "Google Scholar"), ("linkedin", "LinkedIn")):
        if entry.get(key):
            links.append(f'<a href="{escape(entry[key])}" target="_blank" rel="noopener">{label}</a>')
    if links:
        parts.append(f'<span class="alumni-entry-links">{" ".join(links)}</span>')
    parts.append("</li>")
    return "".join(parts)


def render_alumni():
    data = json.loads((ROOT / "data/alumni.json").read_text())
    entries = [entry for category in data["categories"] for entry in category["entries"]]
    categories = [
        ("Postdoctoral Fellows", lambda role: "postdoctoral" in role.lower()),
        ("Graduate Students", lambda role: role in {"Graduate Student", "PhD Student"}),
        ("Research Scientists", lambda role: role == "Research Scientist"),
        ("Visiting Scientists", lambda role: role == "Visiting Scientist"),
        ("Lab Managers and Technical Staff", lambda role: role == "Staff"),
    ]
    groups = []
    assigned = set()
    grouped_entries = []
    for title, matches in categories:
        matched = [entry for entry in entries if matches(entry.get("role", ""))]
        assigned.update(id(entry) for entry in matched)
        grouped_entries.append((title, matched))
    grouped_entries.append(("Other Alumni", [entry for entry in entries if id(entry) not in assigned]))
    for title, entries_in_group in grouped_entries:
        rendered = "\n".join(alumni_entry(entry) for entry in sorted(entries_in_group, key=lambda item: item["name"].lower()))
        groups.append(
            f'<section class="alumni-group">\n<h3>{escape(title)}</h3>\n'
            f'<ul class="alumni-list">\n{rendered}\n</ul>\n</section>'
        )
    people = ROOT / "people.md"
    text = people.read_text()
    start = "<!-- ALUMNI:START -->"
    end = "<!-- ALUMNI:END -->"
    before, remainder = text.split(start, 1)
    _, after = remainder.split(end, 1)
    grouped_html = "\n".join(groups)
    people.write_text(f"{before}{start}\n{grouped_html}\n{end}{after}")


def render_pages():
    for page in OUTPUT_PAGES:
        subprocess.run([
            "pandoc", f"{page}.md", "-f", "markdown+yaml_metadata_block+raw_html",
            "-t", "html5", "--template=page-template.html", "--standalone",
            "-o", f"{page}.html",
        ], cwd=ROOT, check=True)


def render_sitemap():
    priorities = {"index": "1.0", "research": "0.9", "people": "0.9", "publications": "0.9", "resources": "0.9"}
    urls = []
    for page in PAGES:
        modified = datetime.fromtimestamp((ROOT / f"{page}.md").stat().st_mtime).date().isoformat()
        loc = "https://hogeneschlab.org/" if page == "index" else f"https://hogeneschlab.org/{page}.html"
        frequency = "weekly" if page == "index" else "monthly"
        priority = priorities.get(page, "0.7")
        urls.append(
            f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{modified}</lastmod>\n"
            f"    <changefreq>{frequency}</changefreq>\n    <priority>{priority}</priority>\n  </url>"
        )
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += "\n".join(urls) + "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sitemap)


if __name__ == "__main__":
    render_alumni()
    render_pages()
    render_sitemap()

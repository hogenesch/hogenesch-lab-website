#!/usr/bin/env python3
"""Generate the Circadian Papers page and RSS from approved selections only."""
from datetime import date, datetime, time, timezone
from email.utils import format_datetime
from html import escape
import json
from pathlib import Path
import re
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
SITE = "https://hogeneschlab.org"
SLUG = "circadian-papers"
TITLE = "Circadian Papers"
DESCRIPTION = "Selected new research on biological time, from clocks and genomics to sleep, metabolism, and medicine."


def render(root=ROOT):
    issues = json.loads((root / "data/circadian-papers.json").read_text(encoding="utf-8"))["issues"]
    seen_ids, seen_dates = set(), set()
    items, editions = [], []
    for issue in sorted(issues, key=lambda i: i["date"], reverse=True):
        day = date.fromisoformat(issue["date"])
        published = day.isoformat()
        if published in seen_dates or not 1 <= len(issue["papers"]) <= 5:
            raise ValueError("Use one edition per date and 1 to 5 approved papers per edition")
        seen_dates.add(published)
        cards = []
        for paper in issue["papers"]:
            key, url = paper["id"], paper["url"]
            parsed = urlsplit(url)
            fields = ("title", "citation", "finding", "why", "caveat")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", key) or key in seen_ids:
                raise ValueError(f"Invalid or duplicate paper ID: {key}")
            if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
                raise ValueError(f"{key}: link must be a public HTTPS source")
            if any(not isinstance(paper[f], str) or not paper[f].strip() for f in fields):
                raise ValueError(f"{key}: all editorial fields must be filled")
            if paper["type"] not in {"Peer-reviewed", "Preprint"}:
                raise ValueError(f"{key}: set the publication type")
            seen_ids.add(key)
            p = {k: escape(v) for k, v in paper.items()}
            cards.append(
                f'<article class="callout" id="{key}"><h3>{p["title"]}</h3>'
                f'<p><strong>{p["type"]}</strong> · {p["citation"]}</p>'
                f'<p>{p["finding"]}</p><p><strong>Why it matters:</strong> {p["why"]}</p>'
                f'<p><strong>Keep in mind:</strong> {p["caveat"]}</p>'
                f'<p><a href="{p["url"]}">Read the original paper</a></p></article>'
            )
            # Plain text avoids embedding markup or article excerpts in RSS.
            summary = f'{paper["type"]} · {paper["citation"]}. {paper["finding"]} Why it matters: {paper["why"]} Keep in mind: {paper["caveat"]}'
            items.append((key, paper["title"], day, summary))
        display_day = f"{day.strftime('%B')} {day.day}, {day.year}"
        editions.append(
            f'<section aria-labelledby="edition-{published}"><h2 id="edition-{published}">'
            f'<time datetime="{published}">{display_day}</time></h2>' + "\n".join(cards) + "</section>"
        )

    publication = (root / "publications.html").read_text(encoding="utf-8")
    masthead = publication.split('<main>\n', 1)[1].split('<header', 1)[0]
    masthead = masthead.replace('class="active" href="publications.html"', 'href="publications.html"')
    masthead = masthead.replace("</nav>\n</div>", f'<a class="active" aria-current="page" href="{SLUG}.html">{TITLE}</a>\n</nav>\n</div>')
    head = (root / "page-template.html").read_text(encoding="utf-8")
    head, tail = head.split("$body$", 1)
    head = re.sub(r'\$if\(\w+\)\$.*?\$else\$(.*?)\$endif\$', r'\1', head, flags=re.S)
    meta = {"$title$": f"{TITLE} | Hogenesch Lab", "$permalink$": f"/{SLUG}.html"}
    # Prefer the feed-specific description over the template's generic fallback.
    head = head.replace("Hogenesch Lab studies circadian biology, systems biology, and circadian medicine across clocks, transcriptomes, and public resources.", DESCRIPTION)
    for var, val in meta.items():
        head = head.replace(var, escape(val.removesuffix(" | Hogenesch Lab") if var == "$title$" else val))
    head = head.replace("</head>", f'  <link rel="alternate" type="application/rss+xml" title="{TITLE} | Hogenesch Lab" href="{SLUG}.xml">\n</head>')
    header = (
        '<header class="page-header" id="page-content"><p class="eyebrow">Research Digest</p>'
        f'<h1>{TITLE}</h1><p class="lede">{DESCRIPTION}</p>'
        '<p>Each selection explains what the study found, why it matters, and what to keep in mind. Preprints are labeled.</p>'
        f'<p><a href="{SLUG}.xml">Subscribe via RSS</a></p></header>'
    )
    content = "\n".join(editions) or '<section class="callout"><h2>First selections coming soon</h2><p>New selections will appear here after editorial review.</p></section>'
    (root / f"{SLUG}.html").write_text(head + masthead + header + "\n" + content + tail, encoding="utf-8")

    rss = ET.Element("rss", version="2.0", attrib={"xmlns:atom": "http://www.w3.org/2005/Atom"})
    channel = ET.SubElement(rss, "channel")
    url = f"{SITE}/{SLUG}.html"
    for tag, value in (("title", f"{TITLE} | Hogenesch Lab"), ("link", url), ("description", DESCRIPTION), ("language", "en")):
        ET.SubElement(channel, tag).text = value
    ET.SubElement(channel, "atom:link", href=f"{SITE}/{SLUG}.xml", rel="self", type="application/rss+xml")
    for key, title, day, summary in items:
        item = ET.SubElement(channel, "item")
        link = f"{url}#{key}"
        ET.SubElement(item, "title").text = title
        ET.SubElement(item, "link").text = link
        ET.SubElement(item, "guid", isPermaLink="true").text = link
        ET.SubElement(item, "pubDate").text = format_datetime(datetime.combine(day, time(), timezone.utc), usegmt=True)
        ET.SubElement(item, "description").text = summary
    ET.indent(rss)
    ET.ElementTree(rss).write(root / f"{SLUG}.xml", encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    render()

# Hogenesch Lab Static Site

Minimal GitHub Pages-ready site for the Hogenesch Lab.

## Structure

- `index.md` homepage
- `research.md` research overview
- `people.md` lab structure and current-page placeholders
- `lineage.md` scientific lineage and mentor acknowledgment
- `data/alumni.json` structured alumni records used to maintain the alumni section
- `build_site.py` renders alumni, all HTML pages, and current sitemap dates
- `collaborations.md` long-term scientific partnerships and shared outputs
- `publications.md` selected landmark papers
- `press.md` selected press coverage and image links for published work
- `resources.md` software, databases, and analysis resources
- `join.md` contact and recruiting page
- `404.md` custom not-found page for legacy and mistyped URLs
- `page-template.html` shared Pandoc template
- `styles.css` shared site styling
- `assets/images/` logos and scientific figure assets
- `MIGRATION_NOTES.md` reconstruction notes and manual review items

## Deployment

The published site is plain static HTML served by GitHub Pages with `.nojekyll`.
Markdown pages are the editable source; matching `.html` files are generated before publish.

To regenerate the site locally:

1. Edit the relevant Markdown or data file.
2. Run `python3 build_site.py`.
3. Review and push the updated source, HTML, sitemap, assets, and stylesheet.

## Maintenance

- Keep content in Markdown unless HTML is needed for simple layout blocks.
- Prefer short, durable prose over institution-specific marketing copy.
- Update `people.md` and `join.md` when roster, affiliations, or contact details change.
- Update `data/alumni.json` for alumni changes; `build_site.py` regenerates the grouped People-page entries.
- Add new images under `assets/images/` and reference them with relative paths.
- Keep primary navigation limited to `Home`, `Research`, `People`, `Publications`, `Resources`, and `Join`.

## Circadian Papers

`data/circadian-papers.json` is the approved public archive, not a shortlist or
draft queue. For each issue, add an ISO date and a `papers` array in editorial
order. Each paper needs a stable lowercase hyphenated `id`, `title`, original
HTTPS `url`, `citation`, `type` (Peer-reviewed or Preprint), and `finding`.
Optional `why` and `caveat` fields add labeled context paragraphs; `link_text`
customizes the source link and includes it in RSS; `byline` adds a sign-off to
both HTML and RSS. Omit unused optional fields. Keep unapproved material outside
this public repository.

Run `python3 build_paper_feed.py` to regenerate the page and RSS without
Pandoc, or run the full site build. Commit the JSON and both generated files
together. Never publish the weekly shortlist by default.

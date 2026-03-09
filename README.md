# Hogenesch Lab Static Site

Minimal GitHub Pages-ready site for the Hogenesch Lab.

## Structure

- `index.md` homepage
- `research.md` research overview
- `people.md` lab structure and current-page placeholders
- `lineage.md` scientific lineage and mentor acknowledgment
- `data/alumni.json` structured alumni records used to maintain the alumni section
- `collaborations.md` long-term scientific partnerships and shared outputs
- `publications.md` selected landmark papers
- `resources.md` software, databases, and analysis resources
- `join.md` contact and recruiting page
- `page-template.html` shared Pandoc template
- `styles.css` shared site styling
- `assets/images/` logos and scientific figure assets
- `MIGRATION_NOTES.md` reconstruction notes and manual review items

## Deployment

The published site is plain static HTML served by GitHub Pages with `.nojekyll`.
Markdown pages are the editable source; matching `.html` files are generated before publish.

To regenerate pages locally:

1. Edit the relevant `.md` file.
2. Run `pandoc <page>.md -f markdown+yaml_metadata_block+raw_html -t html5 --template=page-template.html --standalone -o <page>.html`.
3. Push the updated `.md`, `.html`, assets, and `styles.css`.

## Maintenance

- Keep content in Markdown unless HTML is needed for simple layout blocks.
- Prefer short, durable prose over institution-specific marketing copy.
- Update `people.md` and `join.md` when roster, affiliations, or contact details change.
- Update `data/alumni.json` and the alumni block in `people.md` together when verifying former lab members.
- Add new images under `assets/images/` and reference them with relative paths.
- Keep navigation limited to `Home`, `Research`, `People`, `Scientific Lineage`, `Collaborations`, `Publications`, `Resources`, `CircaDB`, and `Join`.

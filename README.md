# Hogenesch Lab Static Site

Minimal GitHub Pages-ready site for the Hogenesch Lab.

## Structure

- `index.md` homepage
- `research.md` research overview
- `people.md` lab structure and selected trainees/alumni
- `publications.md` representative reading list
- `resources.md` software, databases, and analysis resources
- `join.md` contact and recruiting page
- `styles.css` shared site styling
- `assets/images/` logos and scientific figure assets
- `MIGRATION_NOTES.md` reconstruction notes and manual review items

## Deployment

The Markdown pages include Jekyll front matter so GitHub Pages can render them directly.
No framework or build step is required.

To publish on GitHub Pages:

1. Push the repository to GitHub.
2. Enable Pages for the `main` branch at the repository root.
3. The site will render from the Markdown pages and `styles.css`.

## Maintenance

- Keep content in Markdown unless HTML is needed for simple layout blocks.
- Prefer short, durable prose over institution-specific web copy.
- Update `people.md` and `join.md` when roster, affiliations, or contact details change.
- Add new images under `assets/images/` and reference them with relative paths.

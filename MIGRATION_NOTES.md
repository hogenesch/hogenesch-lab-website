# Migration Notes

## What changed

This repository was converted into a minimal static site designed for GitHub Pages and
long-term maintenance. The new site uses a small set of Markdown pages plus one shared
stylesheet and a narrow `assets/images/` directory.

## Important constraint

No actual WordPress tree or clear legacy website mirror was present in the current checkout.
Searches of the working directory did not find `wp-content`, `wp-admin`, `wp-includes`,
`wp-config.php`, exported XML, or other recognizable WordPress artifacts. Because of that,
this migration is a reconstruction from local Hogenesch-related source materials rather than
a literal page-for-page conversion of a legacy site.

## Local sources used

- `cv_letter_seed/John_Hogenesch_Self_Letter_v1.txt`
- `cv_letter_seed/Hogenesch_seed_letter_clean.txt`
- `cv_letter_seed/style_memory_me_letters.json`
- `cv_letter_seed/style_memory_people_letters_only.json`
- `hogenesch_cchmc_scripps_template/make_hogenesch_cchmc_scripps_template.py`
- `hogenesch_cchmc_scripps_template/assets/cchmc_logo.png`
- `hogenesch_cchmc_scripps_template/assets/scripps_logo.png`
- `Oslops_ref/README.md`
- `preOslops/README.md`

## Content decisions

- The homepage was rewritten around three stable themes: circadian biology, systems genomics,
  and circadian medicine.
- The people page preserves durable structure and named trainees/alumni recoverable from local
  materials instead of asserting a fully current roster.
- The publications page is a representative reading list, not a complete CV bibliography.
- The resources page preserves key published tools and databases repeatedly referenced in local
  materials: JTK_CYCLE, PSEA, MetaCycle, CYCLOPS, CircaDB, Gene Atlas, and Gene Wiki.

## Repository hygiene

- Added a root `.gitignore` that ignores the unrelated working directories already present in
  this workspace so the migration commit only captures the site.
- Replaced the prior root `README.md` with site-specific documentation.

## Manual review items

- Confirm whether `john.hogenesch@cchmc.org` is still the desired public contact address.
- Review `people.md` against any unavailable legacy members page if a current roster is needed.
- Decide whether both institutional logos should remain public on the site.
- If a true legacy site export exists elsewhere, compare it against this reconstruction and pull
  over any missing public-facing historical content.

# franciscozorrilla.github.io

Source for [franciscozorrilla.github.io](https://franciscozorrilla.github.io): a single-page CV.

## Architecture

Static HTML, no build step. The page is `index.html` with inline CSS and JS; external dependencies are limited to Google Fonts, [D3 v7](https://d3js.org/) (collaboration graph), the [Altmetric](https://www.altmetric.com/) badge loader, and a [GoatCounter](https://www.goatcounter.com/) counter snippet (privacy-friendly analytics — no cookies, no PII).

`.nojekyll` disables GitHub Pages' Jekyll processing, so files are served verbatim.

## Layout

```
index.html              Single-page site (hero, about, CV, work, metaGEM, talks, now, contact)
robots.txt
.nojekyll               Tells GitHub Pages to skip Jekyll
assets/
  cv.pdf                Industry CV (linked from "Download CV" buttons)
  img/
    fz-headshot.jpg     Hero portrait
    favicon.svg         Tab icon
    og-default.svg      1200×630 social card image (og:image / twitter:image)
scripts/
  altmetric_cv.py        Pulls press/social counts from the public Altmetric API
  altmetric_summary.json Per-DOI press + social totals consumed by the work cards
  altmetric_counts.csv   Full per-paper breakdown
  altmetric_counts.md    Markdown view of the same breakdown
  altmetric_raw.json     Raw API responses (debugging)
```

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000/
```

## Deployment

```bash
git push origin main
```

GitHub Pages serves the new commit within ~1 minute.

## Updating the CV PDF

Replace `assets/cv.pdf` with the latest export. The "Download CV" buttons in the hero, CV section, and "Now" section all link to `/assets/cv.pdf`.

## Analytics

[GoatCounter](https://www.goatcounter.com/) tracks page views and a handful of custom events on a privacy-friendly basis (no cookies, no PII, single tiny snippet in `<head>`). Dashboard: [metagenomez.goatcounter.com](https://metagenomez.goatcounter.com).

Tracked beyond plain page views:

- **Conversion events** via `data-goatcounter-click` attributes: `cv-download`, `email-click`, `contact-linkedin`, `contact-github`, `contact-scholar`, `contact-bluesky`, `contact-x`.
- **`contact-intent` composite**: fires once per session on the first occurrence of `cv-download`, `email-click`, or `contact-linkedin` (deduped via `sessionStorage`).
- **Engagement signals**: `view-work`, `view-contact`, `reached-footer` (IntersectionObserver), `expand-work-<id>` (per work-card detail expand, deduped per session).
- **Outbound link bucketing**: `out-paper`, `out-news`, `out-repo`, `out-data`, `out-other` — assigned by hostname regex on any external `<a>` not already tagged.

Implementation lives entirely in `index.html` (snippet at the top of `<head>`, JS module appended to the end-of-body inline `<script>`). A hostname guard prevents events from firing on local previews; GoatCounter's own `localhost` filter is a second layer.

To **stop tracking your own browser**, visit [franciscozorrilla.github.io/?goatcounter=skip](https://franciscozorrilla.github.io/?goatcounter=skip) once per device — GoatCounter writes a localStorage flag and ignores that browser thereafter.

## Refreshing altmetric numbers

Each work card surfaces aggregated **press** (news + blogs + videos) and **social** (X/Bluesky/Facebook/Reddit/Mastodon) counts from the public Altmetric API.

```bash
pip install requests
python3 scripts/altmetric_cv.py
```

This rewrites `scripts/altmetric_summary.json`, `altmetric_counts.csv`, `altmetric_counts.md`, and `altmetric_raw.json`. Then update each card's `data-press` / `data-social` attributes and the `.card-metrics` row in `index.html` to match.

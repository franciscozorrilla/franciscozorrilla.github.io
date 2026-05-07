# franciscozorrilla.github.io

Source for [franciscozorrilla.github.io](https://franciscozorrilla.github.io) — a single-page CV.

## Architecture

Static HTML, no build step. The page is `index.html` with inline CSS and JS; external dependencies are limited to Google Fonts, [D3 v7](https://d3js.org/) (collaboration graph), and the [Altmetric](https://www.altmetric.com/) badge loader.

`.nojekyll` disables GitHub Pages' Jekyll processing — files are served verbatim.

## Layout

```
index.html              Single-page site (hero, about, CV, work, metaGEM, talks, now, contact)
404.html                404 page
robots.txt
.nojekyll               Tells GitHub Pages to skip Jekyll
assets/
  cv.pdf                Industry CV (linked from "Download CV" buttons)
  img/
    fz-headshot.jpg     Hero portrait
    favicon.svg         Tab icon
    og-default.svg      1200×630 social card image (og:image / twitter:image)
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

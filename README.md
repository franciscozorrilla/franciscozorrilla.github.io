# franciscozorrilla.github.io

Source for [franciscozorrilla.github.io](https://franciscozorrilla.github.io).

## Local development

```bash
bundle install                              # one-time
bundle exec jekyll serve --livereload       # http://127.0.0.1:4000
```

Add `--drafts` to preview drafts. Add `--incremental` for faster rebuilds.

## Editing content

Most content lives in YAML data files and case-study Markdown:

- `_data/site.yml` — tagline, status pill, hire pitch, social links
- `_data/impact.yml` — homepage stat numbers
- `_data/metagem.yml` — metaGEM live stats (refresh ~monthly)
- `_data/skills.yml` — grouped skill matrix
- `_data/talks.yml` — conferences, teaching, mentorship
- `_data/awards.yml` — awards
- `_work/<slug>.md` — one case study per published paper (Scholar 1:1)
- `_posts/<date>-<slug>.md` — blog posts

Page templates: `index.html`, `metagem.html`, `work.html`, `cv.html`, `talks.html`, `now.html`, `contact.html`, `blog.html`, `404.html`.

Layouts in `_layouts/`. Reusable partials in `_includes/`. Styling in `_sass/`.

## Refreshing metaGEM stats (monthly)

```bash
curl -s https://api.github.com/repos/franciscozorrilla/metaGEM \
  | python3 -c "import json,sys;d=json.load(sys.stdin);print('stars:',d['stargazers_count']);print('forks:',d['forks_count'])"
```

Update `_data/metagem.yml` (`stars`, `forks`, `last_updated`).

## CV PDFs

Only `Francisco_Zorrilla_Syngenta.pdf` is copied to `assets/cv.pdf` and downloadable. The academic CV is reference-only and lives outside the repo at `~/Documents/GitHub/FZ_CV_academia.pdf`.

## Deployment

`git push origin main` triggers GitHub Pages build. Live in ~1–2 min.

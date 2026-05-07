# Francisco Zorrilla — Static HTML Preview

This is a **fully functional static HTML preview** of the redesigned portfolio site. All pages are self-contained with inline CSS and JavaScript — no build step required.

## Pages

- **index.html** — Homepage with hero, impact metrics, metaGEM flagship strip, featured work, now section, skills, and CTA
- **metagem.html** — Product page for metaGEM with live stats, documentation links, and citation block
- **work.html** — All 12 case studies with tag-based filtering (click tags to filter by topic)
- **cv.html** — Full curriculum vitae, print-friendly
- **talks.html** — Conferences, teaching, mentorship, awards, and open-source teaching repos
- **contact.html** — Contact information and role search context
- **now.html** — Current work (NCCR Flagship, ProstT5 pipeline, role transition)

## Features

✅ **Dark/light mode toggle** — Click the ☀️/🌙 button in the header. Theme persists in localStorage.

✅ **Full responsive design** — Mobile, tablet, desktop layouts all working.

✅ **Tag filtering on /work/** — Click any tag (open-source, agritech, fermentation, etc.) to filter case studies.

✅ **Design system** — Colors, typography (Fraunces, Inter, JetBrains Mono), spacing all match the plan.

✅ **Navigation** — All pages link together. Consistent header and footer across the site.

✅ **Print-friendly** — CV page optimizes for printing (hides nav/footer).

## How to Use

### In the Browser

Open any `.html` file directly in your browser. No server needed. All pages work completely standalone.

Example: 
- Click `index.html` to load the homepage
- Click links in the navigation to jump between pages
- Toggle theme with the ☀️/🌙 button — theme persists across page reloads
- On `/work/`, click tags to filter case studies

### Checking the Design

- **Colors**: Look for the biotech-green accent (#7DD3A0 dark, #1F7A4D light)
- **Typography**: H1–H3 use Fraunces serif; body is Inter; monospace is JetBrains Mono
- **Spacing & layout**: Grid-based, responsive; sections have consistent padding
- **Dark/light mode**: Toggle and refresh a page — your choice persists

## What's Working

- All 7 main pages rendered with full content
- Dark/light mode with localStorage persistence
- Responsive mobile/tablet/desktop layouts
- Tag filtering on work page (click a tag to filter)
- All navigation links
- Hover effects, transitions, interactive elements
- Print styles on CV

## What's Missing (vs. Full Site)

- Interactive D3 metabolic-network animation on homepage (placeholder shown instead)
- Backtick command palette
- Konami code easter egg
- Terminal 404 page
- Blog pages (not in Phase 1 anyway)
- RSS/sitemap (Jekyll-generated)
- Live GitHub stats fetch (hard-coded values in metagem.html)

These are Phase 2–3 enhancements. **This preview proves the design, layout, and core functionality work.**

## Testing Checklist

- [ ] Open index.html — hero loads, impact numbers visible, metaGEM strip prominent, 4 featured work cards
- [ ] Resize to mobile (375px) — layout reflows, readable on phone
- [ ] Click dark/light toggle — theme changes, persists on reload
- [ ] Navigate between pages — all links work
- [ ] On work.html, click a tag (e.g., "agritech") — cards filter instantly
- [ ] Click "All" to reset filter
- [ ] On cv.html, click "Print this page" — print preview shows clean layout
- [ ] Check footer links on every page — all present

## Next Steps

Once you're happy with the preview:

1. **Push to GitHub** — Commit these static files to the repo, then deploy to GitHub Pages
2. **Replace Jekyll with these files** — This preview is the structure you'll keep; Phase 2 just adds the dynamic pieces
3. **Phase 2** — Add remaining case studies, blog, tag filtering enhancements, etc.
4. **Phase 3** — D3 network, easter eggs, polish

---

**Last updated**: May 6, 2026  
Built with vanilla HTML/CSS/JS — no dependencies, no build step.

#!/usr/bin/env python3
"""
altmetric_cv.py
---------------
Pull per-category attention counts from the public Altmetric API
for every paper on franciscozorrilla.github.io.

Since 10 November 2025 the Altmetric Details Page API requires an API key.
Register one (free for academic / non-commercial use) at
https://www.altmetric.com/solutions/altmetric-api/ and export it before
running:

    export ALTMETRIC_API_KEY="…"
    python3 scripts/altmetric_cv.py

Outputs (written next to this script, so cwd doesn't matter):
  - altmetric_summary.json   per-DOI press/social/score (consumed by the site)
  - altmetric_counts.csv     full per-paper breakdown (machine-readable)
  - altmetric_counts.md      pretty markdown table
  - altmetric_raw.json       full API responses (debugging)
"""

import json
import os
import sys
import time
from pathlib import Path

import requests

# (label, DOI) — edit/extend as you like.
# Note: bioRxiv preprints are tracked SEPARATELY from published versions.
PAPERS = [
    ("metaGEM (NAR 2021)",                     "10.1093/nar/gkab815"),
    ("Cheese flavor (Nat Commun 2023)",        "10.1038/s41467-023-41059-2"),
    ("Plastic degraders (mBio 2021)",          "10.1128/mBio.02155-21"),
    ("Soil cross-feeding (bioRxiv 2025)",      "10.1101/2025.01.29.635426"),
    ("OD calibration (Comm Biol 2020)",        "10.1038/s42003-020-01127-5"),
    ("Drug tolerance (Nat Microbiol 2022)",    "10.1038/s41564-022-01072-5"),
    ("Enterobacteriaceae (Nat Microbiol 2025)", "10.1038/s41564-024-01912-6"),
    ("iGEM fluorescence (PLoS ONE 2021)",      "10.1371/journal.pone.0252263"),
    ("FROG (bioRxiv 2024)",                    "10.1101/2024.09.24.614797"),
    ("Hansenula GEM (bioRxiv preprint)",       "10.1101/2021.06.18.448943"),
    ("Hansenula GEM (book chapter)",           "10.1007/978-1-0716-2399-2_16"),
    ("C. difficile (bioRxiv 2024)",            "10.1101/2024.08.29.610284"),
]

# Buckets of metrics. Press = "shown up in journalism / blogs / video".
# Social = "people sharing on social networks".
PRESS_FIELDS = [
    "cited_by_msm_count",       # mainstream news outlets
    "cited_by_feeds_count",     # blogs (incl. science communication)
    "cited_by_videos_count",    # YouTube etc.
]
SOCIAL_FIELDS = [
    "cited_by_tweeters_count",  # X / Twitter
    "cited_by_bluesky_count",   # Bluesky (Altmetric began tracking 2024+)
    "cited_by_fbwalls_count",   # Facebook
    "cited_by_rdts_count",      # Reddit
    "cited_by_msdon_count",     # Mastodon
]

# Full set of count fields we emit to the CSV / md table for transparency.
COUNT_FIELDS = [
    "score",                       # the headline Altmetric Attention Score
    *PRESS_FIELDS,
    *SOCIAL_FIELDS,
    "cited_by_wikipedia_count",
    "cited_by_policies_count",
    "cited_by_patents_count",
    "cited_by_accounts_count",
    "cited_by_posts_count",
    "readers_count",
]

API = "https://api.altmetric.com/v1/doi/{}"
OUT_DIR = Path(__file__).resolve().parent
API_KEY = os.environ.get("ALTMETRIC_API_KEY", "").strip()


def fetch(doi: str) -> dict | None:
    """Return parsed JSON, or None if the paper isn't tracked (HTTP 404)."""
    params = {"key": API_KEY} if API_KEY else None
    r = requests.get(API.format(doi), params=params, timeout=15)
    if r.status_code == 404:
        return None
    if r.status_code == 429:
        time.sleep(60)
        r = requests.get(API.format(doi), params=params, timeout=15)
    r.raise_for_status()
    return r.json()


def safe_int(value) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def main() -> None:
    if not API_KEY:
        print(
            "ERROR: ALTMETRIC_API_KEY is not set.\n"
            "Register at https://www.altmetric.com/solutions/altmetric-api/ then run:\n"
            "  export ALTMETRIC_API_KEY=\"…\"\n"
            "  python3 scripts/altmetric_cv.py",
            file=sys.stderr,
        )
        sys.exit(1)

    rows: list[dict] = []
    raw: dict[str, dict | None] = {}
    summary: dict[str, dict] = {}

    for label, doi in PAPERS:
        print(f"Fetching {label} ...", flush=True)
        try:
            data = fetch(doi)
        except requests.RequestException as e:
            print(f"  ! request failed: {e}")
            data = None
        raw[doi] = data

        if data is None:
            rows.append({"paper": label, "doi": doi, "tracked": False})
            summary[doi] = {
                "label": label,
                "tracked": False,
                "score": 0,
                "press": 0,
                "social": 0,
                "details_url": "",
            }
        else:
            row = {"paper": label, "doi": doi, "tracked": True}
            row.update({k: data.get(k, 0) for k in COUNT_FIELDS})
            row["details_url"] = data.get("details_url", "")
            rows.append(row)

            press_total = sum(safe_int(data.get(f)) for f in PRESS_FIELDS)
            social_total = sum(safe_int(data.get(f)) for f in SOCIAL_FIELDS)
            summary[doi] = {
                "label": label,
                "tracked": True,
                "score": data.get("score", 0),
                "press": press_total,
                "social": social_total,
                "press_breakdown": {f: safe_int(data.get(f)) for f in PRESS_FIELDS},
                "social_breakdown": {f: safe_int(data.get(f)) for f in SOCIAL_FIELDS},
                "details_url": data.get("details_url", ""),
            }

        time.sleep(1.0)  # polite; the public API allows ~1/sec comfortably

    # ---- write outputs --------------------------------------------------
    (OUT_DIR / "altmetric_raw.json").write_text(json.dumps(raw, indent=2))
    (OUT_DIR / "altmetric_summary.json").write_text(json.dumps(summary, indent=2))

    # CSV
    import csv
    headers = ["paper", "doi", "tracked", *COUNT_FIELDS, "details_url"]
    with open(OUT_DIR / "altmetric_counts.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()
        for row in rows:
            w.writerow({h: row.get(h, "") for h in headers})

    # Markdown — compact, focused on the buckets used by the site
    md_cols = [
        ("Paper",     "paper"),
        ("Score",     "score"),
        ("Press*",    "_press_total"),
        ("Social*",   "_social_total"),
        ("News",      "cited_by_msm_count"),
        ("Blogs",     "cited_by_feeds_count"),
        ("Video",     "cited_by_videos_count"),
        ("X/Twitter", "cited_by_tweeters_count"),
        ("Bluesky",   "cited_by_bluesky_count"),
        ("FB",        "cited_by_fbwalls_count"),
        ("Reddit",    "cited_by_rdts_count"),
        ("Mastodon",  "cited_by_msdon_count"),
        ("Mendeley",  "readers_count"),
    ]
    lines = ["| " + " | ".join(h for h, _ in md_cols) + " |",
             "|" + "|".join("---" for _ in md_cols) + "|"]
    for row in rows:
        if not row.get("tracked"):
            cells = [row["paper"]] + ["—"] * (len(md_cols) - 1)
        else:
            row["_press_total"] = sum(safe_int(row.get(f)) for f in PRESS_FIELDS)
            row["_social_total"] = sum(safe_int(row.get(f)) for f in SOCIAL_FIELDS)
            cells = [str(row.get(k, 0) or 0) for _, k in md_cols]
            cells[0] = row["paper"]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    lines.append("\\* Press = News + Blogs + Video. Social = X/Twitter + Bluesky + Facebook + Reddit + Mastodon.")
    (OUT_DIR / "altmetric_counts.md").write_text("\n".join(lines) + "\n")

    print(f"\nDone. Wrote outputs to {OUT_DIR}/")


if __name__ == "__main__":
    main()

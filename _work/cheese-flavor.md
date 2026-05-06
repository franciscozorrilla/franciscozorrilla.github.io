---
title: "Microbial interactions shape cheese flavour formation"
slug: cheese-flavor
order: 2
featured: true
status: published
year: 2023
venue: "Nature Communications"
venue_short: "Nat. Comms."
doi: "10.1038/s41467-023-44059-4"
url: "https://www.nature.com/articles/s41467-023-44059-4"
role: "second author"
authors: "Melkonian C, Zorrilla F, Kjærbølling I, Blasche S, Machado D, Junge M, Soerensen K, Andersen L, Patil KR, Zeidan AA."
citations: 95
oneliner: "Mechanistic metabolic modeling of dairy fermentation, in industrial collaboration with Chr. Hansen."
problem: "Cheese flavor emerges from cross-feeding between microbial species in the starter culture. Empirical optimization is slow, expensive, and doesn't generalize across products — industrial fermenters needed a mechanistic predictor."
approach: "Built community-level genome-scale metabolic models for the cheese microbiome, integrated metabolomic and transcriptomic data, and simulated cross-feeding to predict which species pairings drive flavor compounds."
contribution: "Designed and ran the metabolic-modelling layer: model curation for the relevant species, community simulation, and integration with the experimental metabolomics."
tools: [COBRA Toolbox, Python, multi-omics, FBA, community simulation]
outcome:
  - {metric: "Nat. Comms.", desc: "tier-1 publication"}
  - {metric: "95", desc: "citations"}
  - {metric: "Chr. Hansen", desc: "industrial collaboration"}
industry_relevance: "Direct precedent for translational fermentation work. The same modelling apparatus applies to dairy, brewing, biopharma fermentation, and any commercial process where inter-species metabolic exchange drives product quality."
tags: [fermentation, industry-collab, methods, clinical]
links:
  - {label: "Paper", url: "https://www.nature.com/articles/s41467-023-44059-4"}
---

This was a multi-year industrial collaboration between the Patil lab and Chr. Hansen, the Danish enzyme-and-culture company that supplies a large fraction of the world's commercial cheese starters. The question was deceptively practical: which combinations of species in a starter culture produce flavor compound X, and which produce flavor compound Y?

The answer required moving past 16S surveys and into mechanistic territory. We curated genome-scale metabolic models for the relevant cheese microbiota, fed them metabolomic data from real fermentations, and used community-level FBA to predict cross-feeding flux distributions. Where the model said "species A's secreted metabolite is the substrate that lets species B produce the desired ester," the metabolomics and transcriptomics confirmed it.

The transferable lesson is that constraint-based modelling can drive real product-design decisions in fermentation — not just retrospective explanation. That's exactly the kind of work I'd like to keep doing on the industry side.

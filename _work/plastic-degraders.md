---
title: "Plastic-degrading potential across the global microbiome correlates with recent pollution trends"
slug: plastic-degraders
order: 3
featured: true
status: published
year: 2021
venue: "mBio"
venue_short: "mBio"
doi: "10.1128/mBio.02155-21"
url: "https://doi.org/10.1128/mBio.02155-21"
role: "co-author"
authors: "Zrimec J, Kokina M, Jonasson S, Zorrilla F, Zelezniak A."
citations: 142
oneliner: "Predictive global screen for novel plastic-degrading enzymes — a data-driven approach for industrial bioremediation and sustainability."
problem: "Plastic pollution outpaces our catalog of enzymes that can degrade it. Wet-lab discovery is slow; we needed a way to mine global metagenomic data for novel plastic-degrading enzyme candidates and check whether environmental abundance tracks pollution."
approach: "Built a deep-learning classifier for plastic-degrading enzyme potential, applied it across global ocean and soil metagenomes, and correlated predicted enzyme abundance with regional pollution levels."
contribution: "Contributed to the metagenomic feature engineering and downstream ecological analysis."
tools: [Python, deep learning, metagenomics, statistical modeling]
outcome:
  - {metric: "mBio 2021", desc: "peer-reviewed publication"}
  - {metric: "142", desc: "citations"}
  - {metric: "global scope", desc: "ocean + soil microbiomes"}
industry_relevance: "A working demonstration of how ML over metagenomic data surfaces industrially-relevant biocatalysts. The same playbook supports enzyme discovery for bioremediation, sustainability, and circular-economy chemistry — directly relevant to industrial biotech and chem-tech companies."
tags: [bioremediation, sustainability, AI-ML, methods]
links:
  - {label: "Paper", url: "https://doi.org/10.1128/mBio.02155-21"}
---

The headline result — a strong correlation between predicted plastic-degrading enzyme abundance and regional pollution intensity — was striking, but the methodological story is what travels: ML models trained on a small curated set of known enzymes can rank candidates from billions of metagenome-derived sequences, dramatically narrowing the wet-lab search space.

For an industrial bioremediation team, this is a concrete pattern: the candidate pipeline doesn't need a new wet-lab campaign to start; it can begin from public sequence data and a few hundred labeled examples. That changes the unit economics of enzyme discovery.

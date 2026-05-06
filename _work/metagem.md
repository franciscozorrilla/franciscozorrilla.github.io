---
title: "metaGEM: reconstruction of genome-scale metabolic models directly from metagenomes"
slug: metagem
order: 1
featured: true
status: published
year: 2021
venue: "Nucleic Acids Research"
venue_short: "Nucleic Acids Res."
doi: "10.1093/nar/gkab815"
url: "https://doi.org/10.1093/nar/gkab815"
role: "first author"
authors: "Zorrilla F, Buric F, Patil KR, Zelezniak A."
citations: 125
oneliner: "Open-source Snakemake workflow that turns raw metagenomes into community-level metabolic models. Used by labs worldwide; #3 in the Snakemake catalog."
problem: "Reconstructing genome-scale metabolic models from metagenomes was a multi-week, error-prone process that required deep expertise across a dozen separate tools — putting community-level metabolic insight out of reach for most labs."
approach: "Architected and released metaGEM, a Snakemake-orchestrated end-to-end pipeline that automates quality control, assembly, binning, MAG consolidation, taxonomy assignment, GEM reconstruction, and community simulation. Designed for HPC clusters and reproducible execution."
contribution: "Lead developer and corresponding author. Designed the architecture, wrote the pipeline, authored the documentation, and have maintained the project through five major releases."
tools: [Snakemake, Python, CarveMe, SMETANA, MEGAHIT, metaSPAdes, CONCOCT, MetaBAT2, MetaWRAP, GTDB-Tk, Slurm HPC]
outcome:
  - {metric: "260+", desc: "GitHub stars"}
  - {metric: "#3", desc: "Snakemake catalog"}
  - {metric: "14,000+", desc: "models built across studies"}
  - {metric: "125", desc: "citations"}
  - {metric: "NAR 2021", desc: "tier-1 venue"}
  - {metric: "MIT", desc: "open source"}
industry_relevance: "Demonstrates ability to ship and maintain an open-source bioinformatics product that survives in production. The Snakemake-on-Slurm engineering, environment management, and CI patterns translate directly to industrial pipeline work in agbio, pharma, and biotech R&D."
tags: [open-source, tool-paper, methods, agritech]
links:
  - {label: "GitHub", url: "https://github.com/franciscozorrilla/metaGEM"}
  - {label: "Paper", url: "https://doi.org/10.1093/nar/gkab815"}
  - {label: "metaGEM page", url: "/metagem/"}
---

metaGEM started at EMBL Heidelberg as glue code wrapping CarveMe and SMETANA over a Slurm cluster, and grew into a maintained Snakemake workflow during my PhD at the Patil lab (MRC Toxicology Unit, Cambridge). The bottleneck it removed was real: in 2019, going from a metagenome FASTQ to a usable community-level GEM took weeks of pipelining and debugging, even for an experienced student. Today, a researcher with no metabolic-modelling background can submit one Snakemake job and get reproducible community-level metabolic predictions out the other end.

The key engineering decisions were unfashionable but correct: pin every dependency in conda environments, lean on Snakemake's checkpoints rather than ad-hoc bash, write documentation with the assumption the reader has never used Slurm, and keep the surface area small. Five years on, those decisions are why the workflow still runs.

For an industry team, the artefact to look at is the maintenance pattern as much as the code: the question of "can a single computational scientist ship and maintain a production-quality bioinformatics pipeline that other people actually use" is one I've answered with this project.

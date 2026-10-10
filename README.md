# Can Small Language Models Review Research Papers?

A study of small open LLMs as paper reviewers, using ICLR submissions and their public human reviews.

**Question.** If a small LLM rates the same paper with prompts that mean the same thing, does it give the same verdict — and does that verdict agree with human reviewers?

**Author:** Pawan Chaudhary (Dakota State University) · **Paper:** [`paper/paper-v3.pdf`](paper/paper-v3.pdf)

## Status

| Version | What | Where |
|---|---|---|
| v1 | Pilot: 60 ICLR 2024 papers, Qwen2.5 1.5B/3B, written (greedy) scores. Found that scores collapse onto 8. | `runs/v1_greedy_only.ipynb` |
| v2 | Adds probability-weighted (expected) scores, Qwen2.5-7B, bootstrap CIs. | `notebooks/pilot.ipynb`, `runs/v2_expected_score.ipynb`, `results/` |
| v3 (final) | Fixes a data bug (withdrawn papers had been counted as rejected); 200 papers per year from ICLR 2024 and 2025; adds Phi-3.5-mini, a contamination check, a human ceiling, text baselines, Holm correction, power analysis. | `notebooks/study_v3.ipynb`, `results/*_v3.*`, `paper/paper-v3.pdf` |

## Main results (v3)
- **Too generous:** every model gives a score of 6 or more ("marginally above the acceptance threshold") to 99–100% of papers, although half were rejected.
- **Wording matters:** when each prompt accepts its top half, 24–38% of papers are accepted under one wording and rejected under another (random rankings: 88%).
- **Human ceiling:** on ICLR 2024, Qwen2.5-7B correlates 0.33 with the other reviewers' average, against 0.43 for a single human reviewer. On ICLR 2025 (after the models' training), it falls to 0.28 against 0.52, and the smaller models to near zero.
- **Rewarding hype:** model scores rise with promotional words such as "novel" and "state-of-the-art" (ρ 0.27–0.39); human ratings do not (ρ ≈ 0).
- **Baselines:** a simple TF-IDF classifier matches the best model on ICLR 2025 (AUC 0.63 vs 0.62).

Full tables: `results/tables_v3.md`. Paper tables are generated from `results/metrics_v3.json` by `scripts/make_tables.py`.

## Setup
- **Data:** ICLR 2024 / 2025 submissions with decisions and reviews, from public OpenReview mirrors on Hugging Face (`smallari/openreview-iclr2024-peer-reviews-RAW`, `smallari/openreview-iclr2025-peer-reviews-RAW`), pinned to fixed commits.
- **Models:** Qwen2.5-{1.5B, 3B, 7B}-Instruct and Phi-3.5-mini-instruct, fp16, greedy decoding.
- **Prompts:** four meaning-preserving prompts asking for a 1–10 score from the title and abstract (full text in the paper's appendix).
- **Scores:** the written score, and an expected score Σ s·P(s) from the model's next-token probabilities.

## Reproduce
1. On [Kaggle](https://www.kaggle.com/code): New Notebook → File → Import Notebook → `notebooks/study_v3.ipynb`.
2. Session options: Accelerator **GPU T4 x2**, Internet **On**.
3. Save Version → Save & Run All. Outputs appear under `data/` and `results/`. (The notebook also runs on Google Colab with a T4 GPU.)
4. Locally: `python scripts/make_tables.py` regenerates the paper's tables; compile `paper/overleaf/main.tex` with pdflatex + bibtex.

## Paper
LaTeX source is in `paper/overleaf/`. Every push rebuilds the PDF with GitHub Actions (see the *Build paper* workflow); tagged versions attach the PDF to a release.

## Repository layout
```
notebooks/        Kaggle notebooks (pilot v2, full study v3)
runs/             executed notebooks from earlier runs, kept as a record
data/             sampled papers with human ratings
results/          scores, metrics, tables, figures
paper/overleaf/   LaTeX source, bibliography, figures
paper/            writing notes
scripts/          checks run in CI
```

## AI assistance
Code, analysis, and text were developed with help from an AI assistant (Claude, Anthropic). All content was reviewed by the author.

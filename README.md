# can small language models review research papers?

I wanted to know when you can actually trust what a machine tells you, and paper reviewing felt like a good place to test it. LLMs are already being used to judge research (The AI Scientist uses one to decide which of its own papers are good). So I asked a simple question: if a small, free model that a student can run reads a paper's title and abstract, does its verdict depend on the paper, or on how I phrase the question?

**Paper:** [`paper/paper.pdf`](paper/paper.pdf)
**Author:** Pawan Chaudhary, Dakota State University

## what i did

- took **400 ICLR papers**: 200 from 2024 and 200 from 2025, half accepted and half rejected, with their real public reviews
- had **four small open models** (Qwen2.5 1.5B, 3B, 7B and Phi-3.5-mini) score each one from 1 to 10
- used **four prompts** that ask the exact same question in different words
- compared the models with the real human reviewers, with each other, and with some very simple baselines

The 2025 papers are my contamination check. Their reviews and decisions came out after these models were trained, so the models can't have memorized them.

## what i found

- **They accept almost everything.** Every model gave a passing score (6 or more) to 99–100% of papers, even though half were rejected.
- **The wording changes the verdict.** When each prompt "accepts" its top half, 24–38% of papers are accepted under one wording and rejected under another. (Random rankings would flip 88%, so it isn't random, but it's a lot.)
- **The best model gets part of the way to a human reviewer.** On 2024 papers, Qwen2.5-7B agrees with the other reviewers about three-quarters as well as one human reviewer does (0.33 vs 0.43). On 2025 papers it drops to 0.28 vs 0.52, and the smaller models drop to almost nothing. Part of the 2024 result might come from the models having seen those papers. I can't prove it, but it's the obvious suspect.
- **They reward hype.** Scores go up with words like "novel" and "state-of-the-art". Human ratings don't move at all with those words, and this isn't just longer abstracts having more of them.
- **Counting words does about as well.** On the 2025 papers, a basic word-count classifier separates accepted from rejected papers about as well as the best model.

The full tables are in [`results/summary_tables.md`](results/summary_tables.md).

## what went wrong along the way

I'm keeping these here because they changed the results, and I'd rather be upfront about them:

- my first version used the number the model writes, which was "8" almost every time. I switched to a probability-weighted score.
- in the pilot I counted withdrawn papers as rejected (7 out of 30). Only papers marked exactly "Reject" count now.
- the 7B model crashed twice on the same paper when I scored prompts in batches of four. I re-scored all of it one prompt at a time, then checked whether batching had changed anything: on the 952 prompts scored both ways, the scores differ by 0.003 points on average. So the crash was the real problem, not the numbers.
- Phi writes a space before each digit, and my first full run read its probabilities one step too early. A sanity check caught it, and Phi was re-scored.

The earlier pilot is in [`pilot/`](pilot/), with its own notes.

## what's where

```
notebooks/run_study.ipynb      the whole study, start to finish (runs on Kaggle or Colab)
analysis/                      small scripts that run on a normal laptop
  make_paper_tables.py           builds the paper's tables from the results, so nothing is typed by hand
  extra_analyses.py              follow-up checks (hype vs. length, averaging, batching, power)
  check_outputs.py               sanity checks that run on every push
data/                          the 400 sampled papers with their human ratings, plus all paper IDs
results/                       model scores (with every probability), metrics, tables, figures
paper/paper.pdf                the paper
paper/latex/                   LaTeX source, references, figures, generated tables
pilot/                         the first, smaller version of the study
notes/                         my writing notes and the revision checklist
```

## how to rerun it

1. Upload `notebooks/run_study.ipynb` to [Kaggle](https://www.kaggle.com/code) (New Notebook → File → Import Notebook).
2. Set Accelerator to **GPU T4 x2** and turn Internet **On**.
3. Save Version → Save & Run All. It takes about an hour on Kaggle's free GPUs.
4. On a laptop, with the outputs in place: `python analysis/extra_analyses.py`, then `python analysis/make_paper_tables.py`, then compile `paper/latex/main.tex`.

Models and datasets are pinned to exact versions, and the sampling is seeded, so the same papers and scores come out every time.

## license and citing

- **Code** (`notebooks/`, `analysis/`): MIT license, see [`LICENSE`](LICENSE).
- **Paper, results, and figures** (`paper/`, `results/`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Use them freely, just credit the source.
- **The ICLR titles, abstracts, and review ratings** in `data/` and in the scores files come from OpenReview. They belong to their authors and keep their original terms. I only redistribute them so the study can be checked.

To cite this work, use the **"Cite this repository"** button on GitHub (it reads [`CITATION.cff`](CITATION.cff)).

## being honest about help

I used an AI assistant (Claude, by Anthropic) for code, running analyses, and drafting and editing. The questions, the decisions, and the responsibility for every claim are mine, and I've gone through all of it.

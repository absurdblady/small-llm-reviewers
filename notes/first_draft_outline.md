# Paper writing guide — fill this into Overleaf

**Template:** Overleaf → New Project → Templates → search **"ACL"** → *ACL Rolling Review / ACL 2023 Proceedings Template*.
Use `\usepackage[review]{acl}` while drafting, switch to `\usepackage{acl}` for the preprint.
**Length target:** 4 pages + references. **Write in this order:** Setup → Results → Intro → Related Work → Limitations → Conclusion → Abstract (last!).

Numbers in `[brackets]` come from `results/table.md` / `results/metrics.json`. Never type a number you did not compute.

---

## Title (pick one)
- **Lenient, Prompt-Sensitive, and Weakly Aligned: A Pilot Study of Small LLMs as Paper Reviewers**
- How Stable Are Small LLM Reviewers? A Pilot Study on ICLR 2024 Submissions

## Abstract (write LAST, ~150 words, 5 sentences)
1. Context: LLMs are increasingly used as automated paper reviewers (e.g., The AI Scientist).
2. Gap: prior work varies reviewer configuration, but not whether meaning-preserving rewording of the prompt changes the verdict.
3. What you did: 60 ICLR 2024 submissions (30 accepted, 30 rejected), Qwen2.5 1.5B/3B/7B, four paraphrased prompts, greedy and probability-weighted scores.
4. Findings: all three models give a greedy "accept" (≥6) to **100%** of papers; with relative top-31% verdicts, **18–33%** of papers flip between prompts (random: 76%); agreement with humans is weak (Spearman ≤ 0.24; AUC 0.58–0.70, best at 7B).
5. Implication: single-prompt scores from small LLM reviewers should not be trusted; report multi-prompt results.

## 1 Introduction (~0.75 page, 4 paragraphs)
- **P1 — Motivation.** LLM-as-a-judge reaches ~80% agreement with humans in chat evaluation (Zheng et al. 2023). The AI Scientist (Lu et al. 2024) uses an LLM reviewer, validated on ICLR papers, to decide which generated papers are good; Liang et al. 2024 study LLM feedback on real papers. If the reviewer is unreliable, everything built on it inherits that.
- **P2 — The problem.** LLM judges are swayed by irrelevant features — answer position, verbosity (Zheng et al.) — and LLMs in general by prompt formatting (Sclar et al. 2023; Mizrahi et al. 2024). Prior automated-reviewer work varies the *configuration* (reflection, few-shot, ensembling) but not the *wording* of equivalent prompts. Small open models — the ones students and labs can run — are least studied.
- **P3 — What you did.** Data, 3 models, 4 prompts, 2 scoring methods, 3 measures (leniency, stability, agreement).
- **P4 — Contributions (3 bullets).** (i) small LLM reviewers are uniformly lenient (100% greedy accept vs 50% true); (ii) 18–33% of accept/reject verdicts change with prompt wording alone; (iii) agreement with humans is weak and grows modestly with scale; code + data released.

## 2 Related Work (~0.5 page, 2 short paragraphs)
- **LLM-as-a-judge & automated reviewing:** Zheng et al. 2023 (80% agreement; position, verbosity, self-enhancement biases; reference-guided judging fixes math failures); Lu et al. 2024 (automated reviewer on ~500 ICLR 2022 papers, ≈ human balanced accuracy, but more false accepts — i.e., lenient); Liang et al. 2024.
- **Prompt sensitivity:** Sclar et al. 2023; Mizrahi et al. 2024. Close: *"Prior work varies reviewer configuration but not the wording of semantically equivalent prompts; we study the latter."*

## 3 Experimental Setup (~0.75 page)
- **Data.** ICLR 2024 from `smallari/openreview-iclr2024-peer-reviews-RAW` (public OpenReview mirror); papers with ≥3 reviews; random sample (seed 42), 30 accepted + 30 rejected. Mean human rating: accepted 6.37, rejected 4.62; mean std between a paper's human reviewers 0.89 / 1.00.
- **Models.** Qwen2.5-{1.5B, 3B, 7B}-Instruct (cite Qwen 2024), fp16, Kaggle GPUs.
- **Prompts.** Table: P1 expert role / P2 plain / P3 instruction after content / P4 terse markdown. Full text in Appendix.
- **Scores.** (a) *Greedy*: the integer the model writes. (b) *Expected*: Σ s·P(s) over s=1..10 from next-token probabilities (handle "1" vs "10" with a second step). Why: greedy outputs collapse onto 8, hiding differences.
- **Metrics.** Leniency (share of greedy ≥6); stability (per-paper std of expected score across prompts; mean pairwise Spearman between prompts; flip rate of relative top-31% verdicts, vs random baseline 1−0.31⁴−0.69⁴ = 76%); agreement (Spearman vs mean human rating, AUC accepted vs rejected, 95% bootstrap CIs, 1000 resamples).

## 4 Results (~1 page — the heart of the paper; numbers from results/table.md)
- **4.1 Leniency.** Greedy scores collapse: "8" is 69–86% of outputs; every model gives ≥6 to 100% of papers although only 50% were accepted. Same pattern as the AI Scientist reviewer's excess false accepts.
- **4.2 Stability.** Prompt rankings mostly agree (mean ρ 0.77–0.80, min 0.65), but 18% (7B) to 33% (3B) of papers flip accept/reject between prompts — far below random (76%) but far from stable. Prompts also shift the *level*: mean expected score varies by up to 0.84 points across prompts (3B: 7.75 vs 8.59), larger than the gap that separates many papers → any absolute threshold is prompt-dependent. P4_terse is consistently scored lowest at 7B. **Figure 1.**
- **4.3 Agreement with humans.** Spearman ρ is 0.01–0.24; only 7B + P1 has a CI excluding 0 (0.24 [0.01, 0.45]). AUC rises with scale: ~0.58–0.64 (1.5B), 0.58–0.67 (3B), 0.68–0.70 (7B; CIs exclude 0.5). P3_after (instruction after the paper) gives the lowest ρ at 3B/7B — *suggestive only*, CIs overlap. **Figure 2.**
- **4.4 Averaging.** Prompt-averaged scores match a typical single prompt, not the best one — but the best prompt is only knowable after seeing human labels, so averaging is the safer default.
- Key interpretation sentence: *the models are fairly consistent with themselves yet barely consistent with humans — they rank papers by something other than reviewer-judged quality.*

## 5 Limitations (~0.3 page, bullet list — reviewers love honesty here)
- Small sample (60 papers; balanced, unlike the real 31% acceptance rate), one venue/year, one model family.
- Title + abstract only, not full papers.
- Possible contamination: ICLR 2024 papers/reviews may be in the models' training data.
- Humans use {1,3,5,6,8,10}; LLM expected scores are continuous — std comparisons approximate.
- Several metrics × prompts × models with n=60: individual differences may be noise; no multiple-comparison correction.

## 6 Conclusion (~4 sentences)
Restate the finding, the implication (report multi-prompt scores; don't trust single-prompt LLM reviews), and future work: larger models, full-text reviewing, more perturbation types (section order, formatting), calibration methods.

## Appendix
Full text of the 4 prompts; parse rate per model; per-paper scores link to repo.

---

## References — BibTeX (verify each on arxiv.org before submitting)
```bibtex
@article{zheng2023judging, title={Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena}, author={Zheng, Lianmin and others}, journal={arXiv preprint arXiv:2306.05685}, year={2023}}
@article{lu2024aiscientist, title={The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery}, author={Lu, Chris and others}, journal={arXiv preprint arXiv:2408.06292}, year={2024}}
@article{sclar2023quantifying, title={Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting}, author={Sclar, Melanie and others}, journal={arXiv preprint arXiv:2310.11324}, year={2023}}
@article{mizrahi2024state, title={State of What Art? A Call for Multi-Prompt LLM Evaluation}, author={Mizrahi, Moran and others}, journal={arXiv preprint arXiv:2401.00595}, year={2024}}
@article{liang2023feedback, title={Can Large Language Models Provide Useful Feedback on Research Papers? A Large-Scale Empirical Analysis}, author={Liang, Weixin and others}, journal={arXiv preprint arXiv:2310.01783}, year={2023}}
@article{qwen2024qwen25, title={Qwen2.5 Technical Report}, author={{Qwen Team}}, journal={arXiv preprint arXiv:2412.15115}, year={2024}}
```

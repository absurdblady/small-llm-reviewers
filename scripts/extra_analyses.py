"""Follow-up analyses that need no GPU (run locally after the Kaggle run).

1. Hype words vs. length: correlation of model scores with hype words per 100 words, and a partial
   rank correlation with the hype-word count controlling for abstract length.
2. Averaging prompts: spread of each prompt's expected scores, and a rank-average alternative.
3. Batching check: Qwen2.5-7B expected scores computed in batches of 4 vs. one prompt at a time.
4. Power under the Holm correction.

Usage:  python scripts/extra_analyses.py [old_batched_scores.csv]
Writes results/extra_v3.json.
"""
import json
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm, rankdata, spearmanr

ROOT = Path(__file__).resolve().parent.parent
HYPE = ["novel", "state-of-the-art", "state of the art", "sota", "significantly", "significant", "outperform",
        "outperforms", "superior", "remarkable", "unprecedented", "groundbreaking", "first", "breakthrough",
        "substantially", "dramatically", "promising", "effective", "efficient", "robust"]
PROMPTS = ["P1_expert", "P2_plain", "P3_after", "P4_terse"]
SEVEN_B = "Qwen/Qwen2.5-7B-Instruct"

scores = pd.read_csv(ROOT / "results/scores_v3.csv")
out = {"hype": {}, "averaging": {}, "power": {}}


def partial_spearman(x, y, z):
    """Spearman correlation of x and y after removing the linear effect of z from the ranks of both."""
    rx, ry, rz = rankdata(x), rankdata(y), rankdata(z)
    res = lambda r: r - np.polyval(np.polyfit(rz, r, 1), rz)
    return float(np.corrcoef(res(rx), res(ry))[0, 1])


for year in (2024, 2025):
    papers = pd.read_csv(ROOT / f"data/papers_{year}.csv")
    ab = papers["abstract"].fillna("").str.lower()
    words = ab.str.split().str.len().values.astype(float)
    hype = ab.apply(lambda t: sum(len(re.findall(r"\b" + re.escape(h) + r"\b", t)) for h in HYPE)).values.astype(float)
    rate = hype / words * 100
    human = papers["human_mean"].values
    hy = {"hype_vs_length": spearmanr(hype, words)[0],
          "human": {"hype_count": spearmanr(human, hype)[0], "hype_rate": spearmanr(human, rate)[0],
                    "hype_count_partial_length": partial_spearman(human, hype, words)},
          "models": {}}
    av = {}
    for model, s in scores[scores["year"] == year].groupby("model"):
        wide = s.pivot_table(index="paper_id", columns="prompt_id", values="exp_score").reindex(papers["paper_id"])
        W = wide[PROMPTS].values
        avg = W.mean(1)
        hy["models"][model] = {"hype_count": spearmanr(avg, hype)[0], "hype_rate": spearmanr(avg, rate)[0],
                               "hype_count_partial_length": partial_spearman(avg, hype, words),
                               "length": spearmanr(avg, words)[0]}
        rank_avg = np.mean([rankdata(W[:, j]) for j in range(4)], axis=0)
        av[model] = {"prompt_sd": dict(zip(PROMPTS, W.std(0).round(3).tolist())),
                     "prompt_mean": dict(zip(PROMPTS, W.mean(0).round(3).tolist())),
                     "share_of_average_variance_from_each_prompt": dict(zip(PROMPTS, (
                         np.cov(W.T).sum(1) / np.cov(W.T).sum()).round(3).tolist())),
                     "spearman_score_average": spearmanr(avg, human)[0],
                     "spearman_rank_average": spearmanr(rank_avg, human)[0],
                     "spearman_per_prompt": {p: spearmanr(W[:, j], human)[0] for j, p in enumerate(PROMPTS)}}
    out["hype"][year] = hy
    out["averaging"][year] = av

# power: one test at alpha = 0.05 (no correction) vs. the strictest Holm step over 40 tests per year
def power_at(r, n, alpha):
    z = np.arctanh(r) * np.sqrt(n - 3)
    return float(norm.cdf(z - norm.ppf(1 - alpha / 2)) + norm.cdf(-z - norm.ppf(1 - alpha / 2)))

for r in (0.2, 0.3):
    out["power"][f"r={r}"] = {"uncorrected": power_at(r, 200, 0.05), "holm_strictest_40_tests": power_at(r, 200, 0.05 / 40)}

# batching check
if len(sys.argv) > 1:
    old = pd.read_csv(sys.argv[1])
    old = old[old["model"] == SEVEN_B]
    new = scores[scores["model"] == SEVEN_B]
    m = old.merge(new, on=["year", "paper_id", "prompt_id"], suffixes=("_b4", "_b1"))
    d = (m["exp_score_b4"] - m["exp_score_b1"]).abs()
    out["batching_7b"] = {"n_overlap": int(len(m)), "mean_abs_diff": float(d.mean()), "max_abs_diff": float(d.max()),
                          "share_diff_below_0.01": float((d < 0.01).mean()),
                          "spearman_b4_vs_b1": float(spearmanr(m["exp_score_b4"], m["exp_score_b1"])[0]),
                          "written_score_agreement": float((m["score_b4"] == m["score_b1"]).mean())}

(ROOT / "results/extra_v3.json").write_text(json.dumps(out, indent=1, default=float), encoding="utf-8")
print(json.dumps(out, indent=1, default=float)[:4000])

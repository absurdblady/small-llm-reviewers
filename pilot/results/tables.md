**Table 1. Leniency and stability across prompts**

| Model | Most common greedy score (share) | Greedy 'accept' (≥6) | Exp.-score std across prompts | Prompt rank agreement ρ (mean / min) | Verdict flip rate, top-31% (random) |
|---|---|---|---|---|---|
| Qwen2.5-1.5B | 8 (71%) | 100% | 0.19 | 0.80 / 0.65 | 27% (76%) |
| Qwen2.5-3B | 8 (86%) | 100% | 0.34 | 0.77 / 0.66 | 33% (76%) |
| Qwen2.5-7B | 8 (69%) | 100% | 0.24 | 0.80 / 0.70 | 18% (76%) |

**Table 2. Agreement with human reviewers (expected score, 95% bootstrap CI)**

| Model | Prompt | Mean exp. score | Spearman ρ vs human mean | AUC accepted vs rejected |
|---|---|---|---|---|
| Qwen2.5-1.5B | P1_expert | 8.26 | 0.01 [-0.27, 0.27] | 0.60 [0.46, 0.74] |
| Qwen2.5-1.5B | P2_plain | 8.33 | 0.05 [-0.21, 0.32] | 0.58 [0.42, 0.72] |
| Qwen2.5-1.5B | P3_after | 8.06 | 0.05 [-0.19, 0.28] | 0.64 [0.49, 0.77] |
| Qwen2.5-1.5B | P4_terse | 7.97 | 0.04 [-0.20, 0.29] | 0.60 [0.46, 0.74] |
| Qwen2.5-1.5B | avg of prompts | 8.16 | 0.03 [-0.24, 0.29] | 0.61 [0.47, 0.75] |
| Qwen2.5-3B | P1_expert | 8.59 | 0.16 [-0.05, 0.37] | 0.66 [0.52, 0.80] |
| Qwen2.5-3B | P2_plain | 7.98 | 0.13 [-0.13, 0.37] | 0.58 [0.42, 0.73] |
| Qwen2.5-3B | P3_after | 7.75 | 0.04 [-0.20, 0.30] | 0.67 [0.52, 0.81] |
| Qwen2.5-3B | P4_terse | 7.98 | 0.15 [-0.11, 0.39] | 0.58 [0.43, 0.73] |
| Qwen2.5-3B | avg of prompts | 8.08 | 0.09 [-0.15, 0.32] | 0.64 [0.50, 0.78] |
| Qwen2.5-7B | P1_expert | 8.35 | 0.24 [0.01, 0.45] | 0.70 [0.56, 0.83] |
| Qwen2.5-7B | P2_plain | 8.47 | 0.19 [-0.06, 0.41] | 0.70 [0.56, 0.83] |
| Qwen2.5-7B | P3_after | 8.34 | 0.03 [-0.23, 0.30] | 0.68 [0.53, 0.80] |
| Qwen2.5-7B | P4_terse | 7.89 | 0.15 [-0.09, 0.39] | 0.69 [0.55, 0.81] |
| Qwen2.5-7B | avg of prompts | 8.26 | 0.17 [-0.08, 0.39] | 0.70 [0.57, 0.82] |

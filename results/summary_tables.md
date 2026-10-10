## ICLR 2024 (n = 200)

**Table A. Leniency and stability**

| Model | Most common written score (share) | Written ≥6 | Mean pairwise Spearman between prompts (min) | Flip rate @50% [95% CI] (random) | Flip rate @real rate [95% CI] (random) | Mean-score shift across prompts [95% CI] |
|---|---|---|---|---|---|---|
| Qwen2.5-1.5B | 8 (76%) | 100% | 0.80 (0.67) | 37% [29%, 44%] (88%) | 33% [26%, 39%] (76%) | 0.32 [0.29, 0.35] |
| Qwen2.5-3B | 8 (92%) | 100% | 0.79 (0.71) | 34% [28%, 42%] (88%) | 29% [24%, 36%] (76%) | 0.74 [0.67, 0.81] |
| Phi-3.5-mini | 9 (84%) | 99% | 0.86 (0.76) | 28% [22%, 35%] (88%) | 28% [22%, 35%] (76%) | 0.43 [0.38, 0.50] |
| Qwen2.5-7B | 8 (72%) | 100% | 0.80 (0.68) | 36% [30%, 44%] (88%) | 26% [21%, 34%] (76%) | 0.57 [0.54, 0.61] |

**Table B. Pairwise flip rates @50% (random = 50%)**

| Model | P1_expert~P2_plain | P1_expert~P3_after | P1_expert~P4_terse | P2_plain~P3_after | P2_plain~P4_terse | P3_after~P4_terse |
|---|---|---|---|---|---|---|
| Qwen2.5-1.5B | 16% | 22% | 12% | 27% | 15% | 25% |
| Qwen2.5-3B | 17% | 23% | 12% | 19% | 18% | 27% |
| Phi-3.5-mini | 11% | 19% | 10% | 17% | 13% | 19% |
| Qwen2.5-7B | 14% | 21% | 18% | 22% | 19% | 23% |

**Table C. Agreement with humans** (Spearman vs mean human rating; AUC accepted vs rejected; 95% CI; * = significant after Holm correction)

Human ceiling (one reviewer vs mean of the others): Spearman 0.43 [0.35, 0.51]

| Model | Prompt | Spearman [95% CI] | AUC [95% CI] |
|---|---|---|---|
| Qwen2.5-1.5B | P1_expert | 0.23 [0.10, 0.35] | 0.57 [0.50, 0.66] |
| Qwen2.5-1.5B | P2_plain | 0.14 [0.00, 0.27] | 0.55 [0.47, 0.63] |
| Qwen2.5-1.5B | P3_after | 0.20 [0.05, 0.32] | 0.57 [0.49, 0.65] |
| Qwen2.5-1.5B | P4_terse | 0.20 [0.07, 0.34] | 0.55 [0.47, 0.63] |
| Qwen2.5-1.5B | average | 0.20 [0.07, 0.33] | 0.56 [0.48, 0.64] |
| Qwen2.5-3B | P1_expert | 0.27 [0.15, 0.39]* | 0.61 [0.54, 0.69] |
| Qwen2.5-3B | P2_plain | 0.24 [0.10, 0.37]* | 0.61 [0.53, 0.68] |
| Qwen2.5-3B | P3_after | 0.22 [0.09, 0.34] | 0.62 [0.54, 0.70] |
| Qwen2.5-3B | P4_terse | 0.29 [0.17, 0.40]* | 0.62 [0.54, 0.70] |
| Qwen2.5-3B | average | 0.28 [0.14, 0.40]* | 0.62 [0.55, 0.70] |
| Phi-3.5-mini | P1_expert | 0.22 [0.09, 0.35] | 0.59 [0.51, 0.66] |
| Phi-3.5-mini | P2_plain | 0.22 [0.09, 0.33]* | 0.57 [0.49, 0.65] |
| Phi-3.5-mini | P3_after | 0.14 [0.01, 0.26] | 0.57 [0.49, 0.65] |
| Phi-3.5-mini | P4_terse | 0.17 [0.04, 0.29] | 0.57 [0.49, 0.65] |
| Phi-3.5-mini | average | 0.16 [0.03, 0.28] | 0.57 [0.49, 0.65] |
| Qwen2.5-7B | P1_expert | 0.35 [0.22, 0.46]* | 0.67 [0.59, 0.74]* |
| Qwen2.5-7B | P2_plain | 0.32 [0.19, 0.43]* | 0.65 [0.57, 0.72]* |
| Qwen2.5-7B | P3_after | 0.26 [0.13, 0.39]* | 0.63 [0.56, 0.70] |
| Qwen2.5-7B | P4_terse | 0.33 [0.21, 0.45]* | 0.66 [0.58, 0.72]* |
| Qwen2.5-7B | average | 0.34 [0.22, 0.46]* | 0.67 [0.58, 0.74]* |

**Table D. Same comparison as the human ceiling** (vs mean of the *other* reviewers, prompt-averaged score)

| Model | Model vs others | Human single reviewer vs others |
|---|---|---|
| Qwen2.5-1.5B | 0.19 | 0.43 |
| Qwen2.5-3B | 0.26 | 0.43 |
| Phi-3.5-mini | 0.15 | 0.43 |
| Qwen2.5-7B | 0.33 | 0.43 |

**Table E. Simple baselines (no LLM)**

| Baseline | Spearman vs human | AUC |
|---|---|---|
| abstract_length | 0.08 | 0.48 [0.40, 0.56] |
| hype_words | 0.08 | 0.50 [0.42, 0.58] |
| hype_per_100_words | 0.04 | 0.49 [0.41, 0.57] |
| tfidf_logreg_cv | — | 0.54 [0.50, 0.58] |

**Table F. What do model scores track?** (Spearman of prompt-averaged score with abstract features)

| Model | Abstract length | Hype words | Hype per 100 words |
|---|---|---|---|
| Qwen2.5-1.5B | 0.31 | 0.32 | 0.23 |
| Qwen2.5-3B | 0.13 | 0.37 | 0.33 |
| Phi-3.5-mini | -0.01 | 0.35 | 0.35 |
| Qwen2.5-7B | 0.13 | 0.27 | 0.24 |

Power: with n = 200, power to detect r = 0.2 is 81%, r = 0.3 is 99%. 80% power needs n = 194 (r = 0.2) or 85 (r = 0.3).

## ICLR 2025 (n = 200)

**Table A. Leniency and stability**

| Model | Most common written score (share) | Written ≥6 | Mean pairwise Spearman between prompts (min) | Flip rate @50% [95% CI] (random) | Flip rate @real rate [95% CI] (random) | Mean-score shift across prompts [95% CI] |
|---|---|---|---|---|---|---|
| Qwen2.5-1.5B | 8 (75%) | 100% | 0.78 (0.64) | 36% [30%, 43%] (88%) | 35% [28%, 42%] (78%) | 0.34 [0.31, 0.37] |
| Qwen2.5-3B | 8 (91%) | 100% | 0.76 (0.62) | 38% [31%, 46%] (88%) | 34% [27%, 40%] (78%) | 0.77 [0.71, 0.84] |
| Phi-3.5-mini | 9 (85%) | 99% | 0.87 (0.82) | 24% [18%, 32%] (88%) | 26% [20%, 32%] (78%) | 0.44 [0.35, 0.53] |
| Qwen2.5-7B | 8 (68%) | 100% | 0.78 (0.68) | 36% [30%, 44%] (88%) | 36% [28%, 41%] (78%) | 0.57 [0.54, 0.60] |

**Table B. Pairwise flip rates @50% (random = 50%)**

| Model | P1_expert~P2_plain | P1_expert~P3_after | P1_expert~P4_terse | P2_plain~P3_after | P2_plain~P4_terse | P3_after~P4_terse |
|---|---|---|---|---|---|---|
| Qwen2.5-1.5B | 15% | 22% | 14% | 25% | 14% | 24% |
| Qwen2.5-3B | 15% | 25% | 15% | 27% | 15% | 29% |
| Phi-3.5-mini | 11% | 15% | 10% | 16% | 11% | 16% |
| Qwen2.5-7B | 13% | 24% | 19% | 23% | 13% | 26% |

**Table C. Agreement with humans** (Spearman vs mean human rating; AUC accepted vs rejected; 95% CI; * = significant after Holm correction)

Human ceiling (one reviewer vs mean of the others): Spearman 0.52 [0.45, 0.59]

| Model | Prompt | Spearman [95% CI] | AUC [95% CI] |
|---|---|---|---|
| Qwen2.5-1.5B | P1_expert | 0.12 [-0.02, 0.25] | 0.56 [0.49, 0.64] |
| Qwen2.5-1.5B | P2_plain | 0.09 [-0.04, 0.23] | 0.55 [0.48, 0.64] |
| Qwen2.5-1.5B | P3_after | 0.05 [-0.09, 0.17] | 0.51 [0.43, 0.59] |
| Qwen2.5-1.5B | P4_terse | 0.12 [-0.01, 0.26] | 0.57 [0.50, 0.66] |
| Qwen2.5-1.5B | average | 0.12 [-0.01, 0.25] | 0.56 [0.48, 0.65] |
| Qwen2.5-3B | P1_expert | 0.10 [-0.05, 0.23] | 0.52 [0.44, 0.61] |
| Qwen2.5-3B | P2_plain | 0.17 [0.04, 0.30] | 0.57 [0.49, 0.65] |
| Qwen2.5-3B | P3_after | 0.12 [-0.01, 0.27] | 0.54 [0.46, 0.62] |
| Qwen2.5-3B | P4_terse | 0.16 [0.02, 0.29] | 0.57 [0.48, 0.65] |
| Qwen2.5-3B | average | 0.13 [0.00, 0.26] | 0.55 [0.47, 0.63] |
| Phi-3.5-mini | P1_expert | 0.12 [-0.02, 0.25] | 0.56 [0.48, 0.64] |
| Phi-3.5-mini | P2_plain | 0.15 [0.02, 0.28] | 0.57 [0.49, 0.65] |
| Phi-3.5-mini | P3_after | -0.00 [-0.14, 0.12] | 0.50 [0.42, 0.57] |
| Phi-3.5-mini | P4_terse | 0.13 [-0.02, 0.25] | 0.57 [0.49, 0.65] |
| Phi-3.5-mini | average | 0.04 [-0.10, 0.17] | 0.52 [0.45, 0.60] |
| Qwen2.5-7B | P1_expert | 0.25 [0.12, 0.38]* | 0.61 [0.53, 0.68] |
| Qwen2.5-7B | P2_plain | 0.30 [0.15, 0.43]* | 0.64 [0.57, 0.71]* |
| Qwen2.5-7B | P3_after | 0.16 [0.02, 0.30] | 0.54 [0.47, 0.63] |
| Qwen2.5-7B | P4_terse | 0.35 [0.22, 0.47]* | 0.67 [0.60, 0.75]* |
| Qwen2.5-7B | average | 0.28 [0.15, 0.42]* | 0.62 [0.54, 0.70] |

**Table D. Same comparison as the human ceiling** (vs mean of the *other* reviewers, prompt-averaged score)

| Model | Model vs others | Human single reviewer vs others |
|---|---|---|
| Qwen2.5-1.5B | 0.12 | 0.51 |
| Qwen2.5-3B | 0.12 | 0.52 |
| Phi-3.5-mini | 0.05 | 0.52 |
| Qwen2.5-7B | 0.28 | 0.51 |

**Table E. Simple baselines (no LLM)**

| Baseline | Spearman vs human | AUC |
|---|---|---|
| abstract_length | 0.05 | 0.57 [0.49, 0.65] |
| hype_words | -0.04 | 0.48 [0.40, 0.56] |
| hype_per_100_words | -0.05 | 0.46 [0.37, 0.53] |
| tfidf_logreg_cv | — | 0.63 [0.59, 0.68] |

**Table F. What do model scores track?** (Spearman of prompt-averaged score with abstract features)

| Model | Abstract length | Hype words | Hype per 100 words |
|---|---|---|---|
| Qwen2.5-1.5B | 0.24 | 0.33 | 0.24 |
| Qwen2.5-3B | 0.08 | 0.35 | 0.33 |
| Phi-3.5-mini | -0.04 | 0.39 | 0.39 |
| Qwen2.5-7B | 0.11 | 0.31 | 0.27 |

Power: with n = 200, power to detect r = 0.2 is 81%, r = 0.3 is 99%. 80% power needs n = 194 (r = 0.2) or 85 (r = 0.3).

## Run

```
{
 "python": "3.13.15",
 "torch": "2.11.0+cu128",
 "transformers": "5.16.1",
 "gpu": "Tesla T4",
 "n_gpus": 2,
 "dtype": "float16",
 "models": {
  "Qwen/Qwen2.5-1.5B-Instruct": {
   "revision": "989aa7980e4cf806f80c7fef2b1adb7bc71aa306"
  },
  "Qwen/Qwen2.5-3B-Instruct": {
   "revision": "aa8e72537993ba99e69dfaafa59ed015b17504d1"
  },
  "microsoft/Phi-3.5-mini-instruct": {
   "revision": "2fe192450127e6a83f7441aef6e3ca586c338b77",
   "answer_first_token_ids": {
    "1": [
     29896
    ],
    "2": [
     29906
    ],
    "3": [
     29941
    ],
    "4": [
     29946
    ],
    "5": [
     29945
    ],
    "6": [
     29953
    ],
    "7": [
     29955
    ],
    "8": [
     29947
    ],
    "9": [
     29929
    ]
   },
   "ten_tokens": [
    29896,
    29900
   ],
   "answer_prefix_tokens": [
    29871
   ],
   "minutes": 20.7
  },
  "Qwen/Qwen2.5-7B-Instruct": {
   "revision": "a09a35458c702b33eeacc393d103063234e8bc28"
  }
 },
 "total_minutes": 25.8
}
```

10-check: {'n_written_10': 12, 'mean_p10_when_written_10': 0.7703203366666668, 'mean_p1_when_written_10': 4.62743975e-08}

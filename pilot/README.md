# pilot (the earlier, smaller version)

This folder is the first version of the study, kept on purpose. It is not what the paper's numbers come from, but it is how I got there, and I'd rather show the path than pretend it went straight.

## what's here

| file | what it is |
|---|---|
| `v1_written_scores_run.ipynb` | first run: 60 ICLR 2024 papers, Qwen2.5 1.5B and 3B, only the number each model writes |
| `v2_notebook.ipynb` | second version of the notebook: adds the probability-weighted (expected) score and the 7B model |
| `v2_expected_scores_run.ipynb` | the executed run of v2, with its outputs |
| `data/pilot_60_papers.csv` | the 60 papers used in the pilot |
| `results/` | v2 scores, metrics, tables, and figures |

## what i learned from it

- **The written score is useless on its own.** Both models wrote "8" for almost every paper. That is why the main study uses the expected score.
- **I counted withdrawn papers as rejected.** 7 of the 30 "rejected" papers here had no decision at all. The main study only counts papers that say exactly "Reject". The numbers in this folder still include that mistake.
- **60 papers is too few.** Most confidence intervals crossed zero, so I couldn't tell "no relationship" from "not enough data". The main study uses 200 papers per year.

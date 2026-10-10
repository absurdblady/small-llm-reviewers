# Facts gathered for the v3 paper revision (2026-10-09)

## Versions (Hugging Face commit hashes)
- Dataset 2024: smallari/openreview-iclr2024-peer-reviews-RAW @ 259c437a57a69bd13659daf56c60c678fbfc92cf
- Dataset 2025: smallari/openreview-iclr2025-peer-reviews-RAW @ 94e63f920fdbfad0cb25d5714dd60a8a2fc844fe
- Qwen/Qwen2.5-1.5B-Instruct @ 989aa7980e4cf806f80c7fef2b1adb7bc71aa306
- Qwen/Qwen2.5-3B-Instruct @ aa8e72537993ba99e69dfaafa59ed015b17504d1
- Qwen/Qwen2.5-7B-Instruct @ a09a35458c702b33eeacc393d103063234e8bc28
- microsoft/Phi-3.5-mini-instruct @ 2fe192450127e6a83f7441aef6e3ca586c338b77
- The notebook also records the revisions actually loaded, plus torch/transformers versions, GPU, and minutes per model.

## Chat template
- No system message was passed. Qwen2.5's template then inserts its default system prompt:
  "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."
- Phi-3.5's template adds no system message when none is given.

## Data issue found in v1/v2
- 7 of the 30 "rejected" papers in v1/v2 had NO decision (label 0, empty decision) — likely withdrawn or desk-rejected.
- v3 uses only decision == "Reject" for rejected; papers without a decision are excluded and counted in the data log.

## Licenses
- The dataset card on Hugging Face lists no license. Say so; note reviews are publicly posted on OpenReview.

## Decided after seeing results (state plainly in the paper)
- The expected score was added after v1 showed written scores collapse on 8.
- The 50% cutoff (main) was adopted after feedback that 31% does not match a balanced sample; 31%/32% kept as secondary.
- Phi-3.5-mini added as a second model family; sample increased to 200; ICLR 2025 added as a contamination check.

## Related work (verified)
- Zhou, Chen, Yu 2024. Is LLM a Reliable Reviewer? A Comprehensive Evaluation of LLM on Automatic Paper Reviewing Tasks. LREC-COLING 2024, pp. 9340–9351. https://aclanthology.org/2024.lrec-main.816
- Liu & Shah 2023. ReviewerGPT? An Exploratory Study on Using Large Language Models for Paper Reviewing. arXiv:2306.00622
- D'Arcy, Hope, Birnbaum, Downey 2024. MARG: Multi-Agent Review Generation for Scientific Papers. arXiv:2401.04259
- Jin, Zhao, Wang, Chen, Zhu, Xiao, Wang 2024. AgentReview: Exploring Peer Review Dynamics with LLM Agents. EMNLP 2024. arXiv:2406.12708

## Author line
- Pawan Chaudhary, Dakota State University (no email).

## Clarity items to apply when writing
- One term: "expected score" everywhere.
- Define 6 = "marginally above the acceptance threshold".
- Table column: "Mean pairwise Spearman ρ between prompts".
- Exact flip numbers, not "one in four or five".
- Sec 4.4: cite the "average" rows with numbers.
- Contributions list at end of intro.
- Fix Figure 1 caption quote mark.
- Multiple comparisons: report Holm-corrected significance.

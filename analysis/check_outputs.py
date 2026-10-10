"""Quick checks that run on every push (GitHub Actions).

I added these after a couple of runs went wrong in ways that were easy to miss, so the repo now checks itself:
  1. every notebook opens (valid JSON),
  2. every scores file has the columns I expect and no expected score outside 1-10,
  3. every metrics file is valid JSON,
  4. every figure the paper includes actually exists.

Usage:  python analysis/check_outputs.py
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
problems = []

# 1. notebooks
for nb in sorted(ROOT.glob("notebooks/*.ipynb")) + sorted(ROOT.glob("pilot/*.ipynb")):
    try:
        cells = json.loads(nb.read_text(encoding="utf-8"))["cells"]
        print(f"ok  {nb.relative_to(ROOT)} ({len(cells)} cells)")
    except Exception as e:
        problems.append(f"{nb.relative_to(ROOT)}: {e}")

# 2. scores
for path in sorted(ROOT.glob("results/scores*.csv")) + sorted(ROOT.glob("pilot/results/scores*.csv")):
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    need = {"model", "paper_id", "prompt_id", "score", "exp_score"}
    missing = need - set(rows[0]) if rows else need
    if missing:
        problems.append(f"{path.name}: missing columns {sorted(missing)}")
        continue
    bad = [r for r in rows if r["exp_score"] and not 1 <= float(r["exp_score"]) <= 10]
    if bad:
        problems.append(f"{path.relative_to(ROOT)}: {len(bad)} expected scores outside 1-10")
    print(f"ok  {path.relative_to(ROOT)} ({len(rows)} rows)")

# 3. metrics
for path in sorted(ROOT.glob("results/*.json")) + sorted(ROOT.glob("pilot/results/*.json")):
    try:
        json.loads(path.read_text(encoding="utf-8"))
        print(f"ok  {path.relative_to(ROOT)}")
    except Exception as e:
        problems.append(f"{path.relative_to(ROOT)}: {e}")

# 4. figures used by the paper
tex = (ROOT / "paper/latex/main.tex").read_text(encoding="utf-8")
for line in tex.splitlines():
    if "\\includegraphics" in line and not line.lstrip().startswith("%"):
        fig = line.split("{")[-1].split("}")[0]
        if not (ROOT / "paper/latex" / fig).exists():
            problems.append(f"paper figure not found: {fig}")

if problems:
    print("\nSomething is off:\n  " + "\n  ".join(problems))
    sys.exit(1)
print("\nAll checks passed.")

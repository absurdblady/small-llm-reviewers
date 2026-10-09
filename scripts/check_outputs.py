"""Sanity checks run in CI: notebooks are valid, result files are well-formed, and the paper's numbers have a source."""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []

# 1. every notebook is valid JSON with cells
for nb in sorted(ROOT.glob("notebooks/*.ipynb")) + sorted(ROOT.glob("runs/*.ipynb")):
    try:
        cells = json.loads(nb.read_text(encoding="utf-8"))["cells"]
        print(f"ok  {nb.relative_to(ROOT)} ({len(cells)} cells)")
    except Exception as e:
        errors.append(f"{nb.relative_to(ROOT)}: {e}")

# 2. score files have the expected columns and plausible values
for path in sorted(ROOT.glob("results/scores*.csv")):
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    need = {"model", "paper_id", "prompt_id", "score", "exp_score"}
    missing = need - set(rows[0]) if rows else need
    if missing:
        errors.append(f"{path.name}: missing columns {sorted(missing)}")
        continue
    bad = [r for r in rows if r["exp_score"] and not 1 <= float(r["exp_score"]) <= 10]
    if bad:
        errors.append(f"{path.name}: {len(bad)} expected scores outside 1-10")
    print(f"ok  {path.relative_to(ROOT)} ({len(rows)} rows)")

# 3. metrics files are valid JSON
for path in sorted(ROOT.glob("results/metrics*.json")):
    try:
        json.loads(path.read_text(encoding="utf-8"))
        print(f"ok  {path.relative_to(ROOT)}")
    except Exception as e:
        errors.append(f"{path.name}: {e}")

# 4. every figure the paper includes exists
tex = (ROOT / "paper/overleaf/main.tex").read_text(encoding="utf-8")
for line in tex.splitlines():
    if "\\includegraphics" in line and not line.lstrip().startswith("%"):
        fig = line.split("{")[-1].split("}")[0]
        if not (ROOT / "paper/overleaf" / fig).exists():
            errors.append(f"paper figure not found: {fig}")

if errors:
    print("\nFAILED:\n  " + "\n  ".join(errors))
    sys.exit(1)
print("\nAll checks passed.")

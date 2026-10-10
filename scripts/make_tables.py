"""Build the paper's LaTeX tables from results/metrics_v3.json, so no number is typed by hand.

Usage:  python scripts/make_tables.py            (writes paper/overleaf/tables/*.tex)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
M = json.loads((ROOT / "results/metrics_v3.json").read_text(encoding="utf-8"))
OUT = ROOT / "paper/overleaf/tables"
OUT.mkdir(parents=True, exist_ok=True)

ORDER = ["Qwen/Qwen2.5-1.5B-Instruct", "Qwen/Qwen2.5-3B-Instruct", "Qwen/Qwen2.5-7B-Instruct",
         "microsoft/Phi-3.5-mini-instruct"]
NAME = {"Qwen/Qwen2.5-1.5B-Instruct": "Qwen2.5 1.5B", "Qwen/Qwen2.5-3B-Instruct": "Qwen2.5 3B",
        "Qwen/Qwen2.5-7B-Instruct": "Qwen2.5 7B", "microsoft/Phi-3.5-mini-instruct": "Phi-3.5-mini"}
PROMPT = {"P1_expert": "P1 expert", "P2_plain": "P2 plain", "P3_after": "P3 after", "P4_terse": "P4 terse",
          "average": "Average of four"}
YEARS = ["2024", "2025"]


def pct(x):
    return f"{100 * x:.0f}\\%"


def ci(c, f="{:.2f}"):
    fmt = lambda v: f.format(v).replace("-", "$-$")
    return f"{{\\scriptsize[{fmt(c[0])}, {fmt(c[1])}]}}"


def pct_ci(c):
    return f"{{\\scriptsize[{100 * c[0]:.0f}, {100 * c[1]:.0f}]}}"


def num(v, f="{:.2f}"):
    s = f.format(v)
    if s.lstrip("-").strip("0.") == "":   # avoid printing "-0.00"
        s = s.lstrip("-")
    return s.replace("-", "$-$")


def write(name, body):
    (OUT / f"{name}.tex").write_text(body, encoding="utf-8")
    print("wrote", name)


# Table: leniency + stability, both years
rows = []
for y in YEARS:
    rows.append(f"\\multicolumn{{6}}{{l}}{{\\textit{{ICLR {y}}}}} \\\\")
    for m in ORDER:
        L, S = M["years"][y]["models"][m]["leniency"], M["years"][y]["models"][m]["stability"]
        rows.append(f"{NAME[m]} & {L['written_mode']:.0f} ({pct(L['written_mode_share'])}) & {pct(L['share_written_ge6'])} & "
                    f"{num(S['pairwise_spearman_mean'])} & {pct(S['flip_rate_50'])} {pct_ci(S['flip_rate_50_ci'])} & "
                    f"{num(S['level_shift'])} {ci(S['level_shift_ci'])} \\\\")
    rows.append("\\midrule")
rows = rows[:-1]
write("stability", r"""\begin{tabular}{lccccc}
\toprule
\textbf{Model} & \textbf{Most common} & \textbf{Written} & \textbf{Prompts agree} & \textbf{Verdict flips} & \textbf{Score shift} \\
 & \textbf{written score} & \textbf{score $\ge$6} & \textbf{(mean $\rho$)} & \textbf{(random: 88\%)} & \textbf{across prompts} \\
\midrule
""" + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}\n")

# Table: agreement with humans, both years side by side
rows = []
for m in ORDER:
    for i, p in enumerate(["P1_expert", "P2_plain", "P3_after", "P4_terse", "average"]):
        cells = [NAME[m] if i == 0 else "", PROMPT[p]]
        for y in YEARS:
            a = M["years"][y]["models"][m]["agreement"][p]
            star = lambda k: "$^{*}$" if a[f"{k}_significant_holm"] else ""
            cells += [f"{num(a['spearman'])}{star('spearman')} {ci(a['spearman_ci'])}",
                      f"{num(a['auc'])}{star('auc')} {ci(a['auc_ci'])}"]
        rows.append(" & ".join(cells) + " \\\\")
    rows.append("\\midrule")
hc = {y: M["years"][y]["human_ceiling"] for y in YEARS}
rows.append("Human reviewer & one vs.\\ others & " + " & ".join(
    f"{num(hc[y]['human_single_vs_others'])} {ci(hc[y]['human_ci'])} & ---" for y in YEARS) + " \\\\")
write("agreement", r"""\begin{tabular}{llcccc}
\toprule
 & & \multicolumn{2}{c}{\textbf{ICLR 2024}} & \multicolumn{2}{c}{\textbf{ICLR 2025}} \\
\cmidrule(lr){3-4} \cmidrule(lr){5-6}
\textbf{Model} & \textbf{Prompt} & \textbf{Correlation $\rho$} & \textbf{AUC} & \textbf{Correlation $\rho$} & \textbf{AUC} \\
\midrule
""" + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}\n")

# Table: fair comparison with a single human reviewer + baselines
rows = []
for m in ORDER:
    rows.append(f"{NAME[m]} (average of prompts) & " + " & ".join(
        num(M["years"][y]["models"][m]["ceiling_comparison"]["model_vs_others"]) for y in YEARS) + " \\\\")
rows.append("\\midrule")
rows.append("One human reviewer & " + " & ".join(num(hc[y]["human_single_vs_others"]) for y in YEARS) + " \\\\")
write("ceiling", r"""\begin{tabular}{lcc}
\toprule
\textbf{Scorer} & \textbf{ICLR 2024} & \textbf{ICLR 2025} \\
\midrule
""" + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}\n")

BASE = {"abstract_length": "Abstract length (words)", "hype_words": "Count of hype words",
        "hype_per_100_words": "Hype words per 100 words", "tfidf_logreg_cv": "Word-count classifier (TF-IDF)"}
rows = []
for b, label in BASE.items():
    cells = [label]
    for y in YEARS:
        v = M["years"][y]["baselines"][b]
        c = v.get("auc_ci") or v.get("auc_range_over_10_repeats")
        cells.append(f"{num(v['auc'])} {ci(c)}")
    rows.append(" & ".join(cells) + " \\\\")
rows.append("\\midrule")
for m in ORDER:
    rows.append(f"{NAME[m]} (average of prompts) & " + " & ".join(
        f"{num(M['years'][y]['models'][m]['agreement']['average']['auc'])} {ci(M['years'][y]['models'][m]['agreement']['average']['auc_ci'])}"
        for y in YEARS) + " \\\\")
write("baselines", r"""\begin{tabular}{lcc}
\toprule
\textbf{Predictor of accept vs.\ reject} & \textbf{AUC, ICLR 2024} & \textbf{AUC, ICLR 2025} \\
\midrule
""" + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}\n")

# Table: what scores track -- hype rate, and hype count controlling for length (from extra_analyses.py)
X = json.loads((ROOT / "results/extra_v3.json").read_text(encoding="utf-8"))
rows = []
for m in ORDER:
    cells = [NAME[m]]
    for y in YEARS:
        h = X["hype"][y]["models"][m]
        cells += [num(h["hype_rate"]), num(h["hype_count_partial_length"]), num(h["length"])]
    rows.append(" & ".join(cells) + " \\\\")
rows.append("\\midrule")
cells = ["Human mean rating"]
for y in YEARS:
    h = X["hype"][y]["human"]
    cells += [num(h["hype_rate"]), num(h["hype_count_partial_length"]),
              num(M["years"][y]["baselines"]["abstract_length"]["spearman_vs_human"])]
rows.append(" & ".join(cells) + " \\\\")
write("tracks", r"""\begin{tabular}{lcccccc}
\toprule
 & \multicolumn{3}{c}{\textbf{ICLR 2024}} & \multicolumn{3}{c}{\textbf{ICLR 2025}} \\
\cmidrule(lr){2-4} \cmidrule(lr){5-7}
\textbf{Correlation of \ldots\ with} & \textbf{hype rate} & \textbf{hype $|$ length} & \textbf{length} & \textbf{hype rate} & \textbf{hype $|$ length} & \textbf{length} \\
\midrule
""" + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}\n")

# Table: pairwise flip rates at the 50% cutoff (random = 50%)
PAIRS = ["P1_expert~P2_plain", "P1_expert~P3_after", "P1_expert~P4_terse",
         "P2_plain~P3_after", "P2_plain~P4_terse", "P3_after~P4_terse"]
SHORT = lambda pair: "--".join(x.split("_")[0] for x in pair.split("~"))
rows = []
for y in YEARS:
    rows.append(f"\\multicolumn{{7}}{{l}}{{\\textit{{ICLR {y}}}}} \\\\")
    for m in ORDER:
        f = M["years"][y]["models"][m]["stability"]["pairwise_flip_50"]
        rows.append(NAME[m] + " & " + " & ".join(pct(f[p]) for p in PAIRS) + " \\\\")
    rows.append("\\midrule")
rows = rows[:-1]
write("pairwise", "\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & "
      + " & ".join(f"\\textbf{{{SHORT(p)}}}" for p in PAIRS) + " \\\\\n\\midrule\n" + "\n".join(rows)
      + "\n\\bottomrule\n\\end{tabular}\n")

"""utils.py — shared helpers imported by the pipeline notebooks.

    import sys; sys.path.append('../src')
    from utils import PATHS, extract_hr, save_fig
"""
from pathlib import Path

# ---- paths (edit only here) -------------------------------------------------
_ROOT = Path(__file__).resolve().parents[1]
PATHS = {
    "raw":     str(_ROOT / "data" / "raw"),
    "derived": str(_ROOT / "data" / "derived"),
    "figures": str(_ROOT / "output" / "figures"),
    "tables":  str(_ROOT / "output" / "tables"),
}

# ---- phenotype conventions (keep consistent across every figure/table) ------
PHENOTYPE_ORDER = ["SIDD", "MARD", "SOIRD"]
PHENOTYPE_COLORS = {          # match the manuscript figures
    "SIDD":  "#1f6fb4",       # blue
    "MARD":  "#8c5a3c",       # brown
    "SOIRD": "#17becf",       # cyan
}
CLUSTER_TO_PHENOTYPE = {1: "SIDD", 2: "MARD", 3: "SOIRD"}  # VERIFY mapping


# ---- tidy a fitted Cox model into HR / CI / p -------------------------------
def extract_hr(fitter, term):
    """Return dict(HR, CI_lower, CI_upper, p_value) for one term.

    Works with a lifelines CoxPHFitter. Adapt the attribute access if you
    use statsmodels PHReg instead.
    """
    s = fitter.summary  # DataFrame indexed by covariate
    row = s.loc[term]
    return {
        "HR":       float(row["exp(coef)"]),
        "CI_lower": float(row["exp(coef) lower 95%"]),
        "CI_upper": float(row["exp(coef) upper 95%"]),
        "p_value":  float(row["p"]),
    }


# ---- consistent figure saving ----------------------------------------------
def save_fig(fig, name, dpi=300, **kwargs):
    """Save to output/figures/<name>.png. Extra kwargs pass to savefig,
    so save_fig(fig, 'x', bbox_inches='tight') works."""
    out = Path(PATHS["figures"]) / f"{name}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=dpi, **kwargs)
    return out

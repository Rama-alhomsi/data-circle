"""Small statistics helpers for the hypothesis tests (Sprint 1).

Why effect sizes?  With 26,707 respondents almost every difference is "statistically significant"
(tiny p-value), even when it is practically irrelevant. So we always report an EFFECT SIZE
(Cramer's V, difference in percentage points, odds ratio) next to the p-value.
"""
import numpy as np
import pandas as pd
from scipy import stats

TARGETS = ["h1n1_vaccine", "seasonal_vaccine"]


def _as_groups(series: pd.Series) -> pd.Series:
    """Treat missing answers as their own group (so nobody is silently dropped)."""
    return series.astype("object").where(series.notna(), "Missing").astype(str)


def cramers_v(df: pd.DataFrame, col: str, target: str):
    """Association between a feature and a 0/1 target. Returns (Cramer's V, p-value).

    V = 0 means no association, V = 1 a perfect one.
    Rough guide for survey data: < 0.1 weak, 0.1-0.3 moderate, > 0.3 strong.
    """
    table = pd.crosstab(_as_groups(df[col]), df[target])
    chi2, p, _, _ = stats.chi2_contingency(table, correction=False)
    k = min(table.shape) - 1
    return float(np.sqrt(chi2 / (table.values.sum() * k))), float(p)


def association_table(df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
    """Cramer's V and p-value of every feature against both targets."""
    rows = []
    for col in features:
        row = {"feature": col}
        for t in TARGETS:
            v, p = cramers_v(df, col, t)
            row[f"V {t.split('_')[0]}"] = round(v, 3)
            row[f"p {t.split('_')[0]}"] = p
        rows.append(row)
    return pd.DataFrame(rows).set_index("feature")


def rate_difference(df: pd.DataFrame, col: str, target: str) -> dict:
    """Vaccination rate for col == 1 vs col == 0, difference in percentage points, 95 % CI."""
    g = df.groupby(col)[target].agg(["sum", "count"])
    p1, n1 = g.loc[1.0, "sum"] / g.loc[1.0, "count"], g.loc[1.0, "count"]
    p0, n0 = g.loc[0.0, "sum"] / g.loc[0.0, "count"], g.loc[0.0, "count"]
    se = np.sqrt(p1 * (1 - p1) / n1 + p0 * (1 - p0) / n0)
    d = p1 - p0
    return {"factor": col, "target": target.split("_")[0],
            "rate if 1 (%)": round(p1 * 100, 1), "rate if 0 (%)": round(p0 * 100, 1),
            "difference (pp)": round(d * 100, 1),
            "CI low": round((d - 1.96 * se) * 100, 1), "CI high": round((d + 1.96 * se) * 100, 1)}


def odds_ratio(df: pd.DataFrame, a: str, b: str) -> dict:
    """Odds ratio (with 95 % CI) and phi for two 0/1 columns."""
    t = pd.crosstab(df[a], df[b])
    or_ = (t.loc[1, 1] * t.loc[0, 0]) / (t.loc[1, 0] * t.loc[0, 1])
    se = np.sqrt((1 / t.values).sum())
    return {"odds ratio": round(or_, 2),
            "CI low": round(float(np.exp(np.log(or_) - 1.96 * se)), 2),
            "CI high": round(float(np.exp(np.log(or_) + 1.96 * se)), 2),
            "phi": round(float(df[[a, b]].corr().iloc[0, 1]), 3)}


def spearman(df: pd.DataFrame, col: str, target: str) -> dict:
    """Rank correlation between an ordered feature and a target (missing rows dropped)."""
    d = df[[col, target]].dropna()
    r, p = stats.spearmanr(d[col], d[target])
    return {"feature": col, "target": target.split("_")[0], "n": len(d),
            "spearman rho": round(float(r), 3), "p": float(p)}

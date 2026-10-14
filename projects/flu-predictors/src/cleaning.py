"""Data cleaning for the Flu Predictors project (shared by Rama and Uyazi).

Design rules
------------
* Every step is a function, so the SAME cleaning can be applied to the training set and the test set.
* Anything LEARNED from data (which job codes are common, the most frequent value per column) is
  learned from the TRAINING set only and then passed to the test set.
* In Sprint 2, `learn_modes` / `fill_numeric` should be replaced by
  `SimpleImputer(strategy="most_frequent")` inside a scikit-learn Pipeline, so the fill value is
  re-learned inside every cross-validation fold.

Typical use
-----------
    keep      = rare_levels(train)
    train_c   = clean(train, keep)
    modes     = learn_modes(train_c)
    train_f   = fill_numeric(train_c, modes)
    test_f    = fill_numeric(clean(test, keep), modes)
    validate(train_f, raw=train); validate(test_f)
"""
import pandas as pd

TARGETS = ["h1n1_vaccine", "seasonal_vaccine"]
ID_COL = "respondent_id"

# --- naming conventions (from Uyazi's notebook) -------------------------------------------------
NOT_EMPLOYED = "Not employed"   # job question does not apply to people who do not work
MISSING = "Missing"             # question was skipped / unknown

# Columns that get a "<col>_missing" flag. All columns with > 5 % missing, except the two job
# columns (their missingness is explained by employment_status), plus the two household counts
# (people who skip them vaccinate much less).
FLAG_COLS = [
    "health_insurance", "doctor_recc_h1n1", "doctor_recc_seasonal", "income_poverty",
    "employment_status", "education", "marital_status", "rent_or_own",
    "household_adults", "household_children",
]
NOT_WORKING = ["Not in Labor Force", "Unemployed"]
JOB_COLS = ["employment_industry", "employment_occupation"]
SPECIAL_LEVELS = {NOT_EMPLOYED, MISSING}

AGE_ORDER = {"18 - 34 Years": 0, "35 - 44 Years": 1, "45 - 54 Years": 2,
             "55 - 64 Years": 3, "65+ Years": 4}
EDU_ORDER = {"< 12 Years": 0, "12 Years": 1, "Some College": 2, "College Graduate": 3}
INCOME_ORDER = {"Below Poverty": 0, "<= $75,000, Above Poverty": 1, "> $75,000": 2}

BINARY_COLS = [
    "behavioral_antiviral_meds", "behavioral_avoidance", "behavioral_face_mask",
    "behavioral_wash_hands", "behavioral_large_gatherings", "behavioral_outside_home",
    "behavioral_touch_face", "doctor_recc_h1n1", "doctor_recc_seasonal",
    "chronic_med_condition", "child_under_6_months", "health_worker", "health_insurance",
]
RANGES = {
    "h1n1_concern": (0, 3), "h1n1_knowledge": (0, 2),
    "opinion_h1n1_vacc_effective": (1, 5), "opinion_h1n1_risk": (1, 5),
    "opinion_h1n1_sick_from_vacc": (1, 5), "opinion_seas_vacc_effective": (1, 5),
    "opinion_seas_risk": (1, 5), "opinion_seas_sick_from_vacc": (1, 5),
    "household_adults": (0, 3), "household_children": (0, 3),
}


# --- 1. tidy text (Uyazi) -----------------------------------------------------------------------
def tidy_text(df: pd.DataFrame) -> pd.DataFrame:
    """Strip and collapse whitespace in text columns (e.g. 'MSA, Not Principle  City')."""
    out = df.copy()
    for col in out.select_dtypes(include=["object", "string"]).columns:
        out[col] = (out[col].astype("string")
                    .str.strip()
                    .str.replace(r"\s+", " ", regex=True))
    return out


# --- 2. range checks / validation (Uyazi's assertions, as reusable functions) --------------------
def check_ranges(df: pd.DataFrame) -> pd.DataFrame:
    """Columns with values outside the expected range (an empty table means everything is fine)."""
    problems = []
    for col in BINARY_COLS:
        if col in df:
            bad = df[col].dropna().loc[lambda s: ~s.isin([0, 1])]
            if len(bad):
                problems.append({"column": col, "bad values": bad.unique().tolist()})
    for col, (lo, hi) in RANGES.items():
        if col in df:
            bad = df[col].dropna().loc[lambda s: (s < lo) | (s > hi)]
            if len(bad):
                problems.append({"column": col, "bad values": bad.unique().tolist()})
    return pd.DataFrame(problems, columns=["column", "bad values"])


def validate(df: pd.DataFrame, raw: pd.DataFrame | None = None, complete: bool = True) -> bool:
    """Raise AssertionError if the cleaned table breaks a basic rule.

    raw      : the untouched table; if given, rows and targets must be unchanged.
    complete : require that no value is missing at all (use after `fill_numeric`).
    """
    ids = df[ID_COL] if ID_COL in df.columns else df.index
    assert ids.is_unique, "respondent ids are not unique"
    if complete:
        assert df.isnull().sum().sum() == 0, "there are still missing values"
    bad = check_ranges(df)
    assert bad.empty, f"values outside the expected range:\n{bad}"
    if raw is not None:
        assert len(df) == len(raw), "number of rows changed"
        for t in TARGETS:
            if t in raw.columns:
                assert (df[t].values == raw[t].values).all(), f"{t} was changed"
    return True


# --- 3. things learned from the TRAINING set ----------------------------------------------------
def rare_levels(train: pd.DataFrame, cols=JOB_COLS, min_count: int = 100) -> dict:
    """Job codes that have at least `min_count` people in the training set."""
    keep = {}
    for col in cols:
        counts = train[col].value_counts()
        keep[col] = set(counts[counts >= min_count].index)
    return keep


def learn_modes(train_clean: pd.DataFrame) -> pd.Series:
    """Most frequent value of every numeric feature (from the cleaned TRAINING set)."""
    cols = [c for c in train_clean.select_dtypes(include="number").columns
            if c not in TARGETS and c != ID_COL and not c.endswith("_missing")
            and c != "n_missing_answers"]
    return train_clean[cols].mode().iloc[0]


# --- 4. cleaning ---------------------------------------------------------------------------------
def clean(df: pd.DataFrame, keep: dict | None = None) -> pd.DataFrame:
    """Clean a copy of the survey data (works for train and test). Numbers are left empty here."""
    out = tidy_text(df)

    # employment_* are excluded from the count: they are missing for everyone who does not work.
    count_cols = [c for c in out.columns if c not in (ID_COL, *TARGETS, *JOB_COLS)]

    # a) count skipped answers and add missing-value flags BEFORE anything is filled
    out["n_missing_answers"] = out[count_cols].isnull().sum(axis=1)
    for col in FLAG_COLS:
        out[f"{col}_missing"] = out[col].isnull().astype("int8")

    # b) job columns: not applicable for people who do not work
    not_working = out["employment_status"].isin(NOT_WORKING)
    for col in JOB_COLS:
        out.loc[not_working & out[col].isnull(), col] = NOT_EMPLOYED

    # c) remaining text gaps -> explicit category
    text_cols = out.select_dtypes(include=["object", "string"]).columns
    out[text_cols] = out[text_cols].fillna(MISSING)

    # d) tiny job codes -> "Other" (levels learned from the training set)
    if keep is not None:
        for col in JOB_COLS:
            allowed = keep[col] | SPECIAL_LEVELS
            out[col] = out[col].where(out[col].isin(allowed), "Other")

    # e) ordered numeric versions of ordinal text columns (originals are kept)
    out["age_group_ord"] = out["age_group"].map(AGE_ORDER)
    out["education_ord"] = out["education"].map(EDU_ORDER)        # "Missing" stays empty
    out["income_ord"] = out["income_poverty"].map(INCOME_ORDER)   # "Missing" stays empty
    return out


def fill_numeric(df: pd.DataFrame, modes: pd.Series) -> pd.DataFrame:
    """Fill empty numeric values with the training-set modes (flags keep the information)."""
    out = df.copy()
    cols = [c for c in modes.index if c in out.columns]
    out[cols] = out[cols].fillna(modes[cols])
    return out

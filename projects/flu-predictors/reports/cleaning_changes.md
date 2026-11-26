# Cleaning notebook: what changed and why

Rama and Uyazi each wrote a `02_data_cleaning` notebook. This note explains how the two were
merged into one shared version (`src/cleaning.py` + `notebooks/02_data_cleaning_rama_uyazi.ipynb`).

## Result of the comparison
Both versions give the same model quality (5-fold logistic regression, ROC AUC):

| Cleaning | H1N1 | Seasonal |
|---|---|---|
| Baseline, no missing-value flags | 0.834 | 0.853 |
| Uyazi's notebook | 0.861 | 0.856 |
| Rama's notebook | 0.862 | 0.856 |
| **Merged version** | **0.862** | **0.856** |

Both approaches found the same key idea (missing-value flags). The merge was about making the
code reusable and combining the best parts, not about one version being wrong.

## What came from Uyazi's notebook
| Idea | Where it is now | Why it is valuable |
|---|---|---|
| Strip and collapse whitespace (`census_msa` double space) | `tidy_text()` | A real data problem the other version missed |
| Missing-value flag for every column with > 5 % missing | `FLAG_COLS` | Simple, rule-based; the flag lifts H1N1 AUC from 0.834 to 0.861 |
| Labels `Not employed` and `Missing` | `NOT_EMPLOYED`, `MISSING` | Clearer than `Not Applicable` / `Unknown`; now the single convention |
| Assertions (no gaps, ranges, targets unchanged) | `validate()` | Catches silent errors; now also works on the test set |
| Fill numeric gaps with the most frequent value | `learn_modes()` + `fill_numeric()` | Gives a model-ready table |
| `respondent_id` as index, before/after rate check | Notebook, sections 7 and 8 | Good habits, kept |

## What was changed, and why
| Change | Why |
|---|---|
| Steps moved from notebook cells into functions in `src/cleaning.py` | The **test set** needs exactly the same cleaning later; functions can be reused, cells cannot |
| Mode values are learned from the training set and passed to the test set (`learn_modes` -> `fill_numeric`) | Avoids leakage and gives the test set identical treatment |
| Added `household_adults/children` flags; dropped the two job-column flags | People who skip the household questions vaccinate far less (seasonal about 26 % vs 47 %); job-column gaps are already explained by `employment_status` |
| Added ordered columns `age_group_ord`, `education_ord`, `income_ord` | The old "ordered" categories were created with `ordered=False`, so the order was not used |
| Added evidence tables (vaccination rate when missing vs answered) | Shows that the flags are justified, not just assumed |
| Added the job-code grouping (ticket 1.7): codes with < 100 people become `Other` | Frequency alone is a bad rule: `haxffmxo` / `dcjcmpih` are rare but have 62 % H1N1 uptake |
| Corrected the notebook text: the mode fill also touches `health_insurance` (46 %) and `doctor_recc_*` (8 %) | The text said "< 5 %", which was not true; it is acceptable only because the flags keep the information |

## Not adopted (yet) and why
- **Small integer and `category` data types:** helpful for memory, but they make the numeric
  columns harder to impute in a Pipeline. Revisit in Sprint 2.
- **Mode fill as the final answer:** fine for exploration, but in Sprint 2 it should be a
  `SimpleImputer` inside the Pipeline so the fill value is re-learned in every CV fold.

## Open points for the two of us
1. Do we agree on `Not employed` / `Missing` as the labels?
2. Is a threshold of 100 people for `Other` sensible, or should we test 50 / 200?
3. Who writes the matching section for `data/processed_data_dictionary.md`?

## How to run
```bash
cd ~/data-circle/projects/flu-predictors
source .venv/bin/activate
jupyter notebook   # open notebooks/02_data_cleaning_rama_uyazi.ipynb
```
Data files must be in `data/` (including `test_set_features.csv`). The cleaned files are written
to `data/processed/` and are ignored by Git.

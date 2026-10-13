# Processed Data Dictionary (modelling dataset)

_To be completed in Sprint 2. Document every transformation so the dataset is reproducible._

| Feature | Derived from | Transformation | Rationale / hypothesis |
|---|---|---|---|
| `preventive_behavior_score` | 7 `behavioral_*` columns | Sum (0–7) | H3: preventive behaviour ↔ uptake |
| `h1n1_risk_perception_score` | `h1n1_concern`, `opinion_h1n1_risk` | Mean after scaling | H4: risk perception |
| `age_group_ord` | `age_group` | Ordinal encoding 0–4 | Preserve order |
| `income_ord` | `income_poverty` | Ordinal encoding 0–2 | Preserve order |
| `<col>_missing` | e.g. `health_insurance` | Binary missing flag | Missingness may be informative |

## Missing-value strategy
| Column | Strategy | Reason |
|---|---|---|
| | | |

## Final files
- `data/processed/train_model_ready.csv` – _description_

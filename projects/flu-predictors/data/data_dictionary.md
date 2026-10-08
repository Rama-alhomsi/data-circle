# Data Dictionary (raw data)

**Source:** National 2009 H1N1 Flu Survey (CDC), via DrivenData
**Download:** https://www.drivendata.org/competitions/66/flu-shot-learning/data/

## Files
| File | Rows | Description |
|---|---|---|
| `training_set_features.csv` | 26,707 | Features for training respondents |
| `training_set_labels.csv` | 26,707 | Targets, joined on `respondent_id` |
| `test_set_features.csv` | 26,708 | Features for test respondents (no labels) |
| `submission_format.csv` | 26,708 | Template: probability per target |

> Note: the project brief mentions `training_set.csv`/`test_set.csv`; the actual download splits features and labels.

## Targets
| Column | Description |
|---|---|
| `h1n1_vaccine` | 1 = received H1N1 vaccine (≈21.2% positive) |
| `seasonal_vaccine` | 1 = received seasonal flu vaccine (≈46.6% positive) |

Correlation between the two targets ≈ 0.38.

## Features (36 columns incl. `respondent_id`)

### Identifier
- `respondent_id` – unique ID (not a feature).

### Opinions / perceptions
| Column | Type | Description |
|---|---|---|
| `h1n1_concern` | ordinal 0–3 | Level of concern about H1N1 (0 = not at all, 3 = very) |
| `h1n1_knowledge` | ordinal 0–2 | Level of knowledge about H1N1 (0 = none, 2 = a lot) |
| `opinion_h1n1_vacc_effective` | ordinal 1–5 | Perceived H1N1 vaccine effectiveness |
| `opinion_h1n1_risk` | ordinal 1–5 | Perceived risk of getting sick with H1N1 without vaccine |
| `opinion_h1n1_sick_from_vacc` | ordinal 1–5 | Worry about getting sick from the H1N1 vaccine |
| `opinion_seas_vacc_effective` | ordinal 1–5 | Perceived seasonal vaccine effectiveness |
| `opinion_seas_risk` | ordinal 1–5 | Perceived risk of getting sick with seasonal flu without vaccine |
| `opinion_seas_sick_from_vacc` | ordinal 1–5 | Worry about getting sick from the seasonal vaccine |

### Behaviours (binary 0/1)
`behavioral_antiviral_meds`, `behavioral_avoidance`, `behavioral_face_mask`, `behavioral_wash_hands`,
`behavioral_large_gatherings`, `behavioral_outside_home`, `behavioral_touch_face`
– whether the respondent took the described preventive action.

### Medical / health access (binary 0/1)
| Column | Description |
|---|---|
| `doctor_recc_h1n1` / `doctor_recc_seasonal` | Doctor recommended the vaccine |
| `chronic_med_condition` | Has chronic medical condition(s) |
| `child_under_6_months` | Regular contact with child < 6 months |
| `health_worker` | Is a health-care worker |
| `health_insurance` | Has health insurance |

### Demographics (categorical)
| Column | Values |
|---|---|
| `age_group` | 18 - 34, 35 - 44, 45 - 54, 55 - 64, 65+ Years |
| `education` | < 12 Years, 12 Years, Some College, College Graduate |
| `race` | White, Black, Hispanic, Other or Multiple |
| `sex` | Female, Male |
| `income_poverty` | Below Poverty, <= $75,000 Above Poverty, > $75,000 |
| `marital_status` | Married, Not Married |
| `rent_or_own` | Own, Rent |
| `employment_status` | Employed, Unemployed, Not in Labor Force |
| `hhs_geo_region` | 10 anonymised HHS regions (random strings) |
| `census_msa` | Non-MSA, MSA Not Principle City, MSA Principle City |
| `household_adults` | Number of other adults in household (0–3) |
| `household_children` | Number of children in household (0–3) |
| `employment_industry` | Anonymised industry codes |
| `employment_occupation` | Anonymised occupation codes |

## Missing Values (training features)
| Column | % missing |
|---|---|
| `employment_occupation` | 50.4% |
| `employment_industry` | 49.9% |
| `health_insurance` | 46.0% |
| `income_poverty` | 16.6% |
| `doctor_recc_*` | 8.1% |
| `rent_or_own` | 7.6% |
| `employment_status` | 5.5% |
| `education`, `marital_status` | 5.3% |
| `chronic_med_condition` | 3.6% |
| `child_under_6_months` | 3.1% |

⚠️ Missingness may itself be informative (e.g. `employment_*` is likely missing for people not in the labour force). Decide per column: impute, "Missing" category, or indicator flag, and document it in `processed_data_dictionary.md`.

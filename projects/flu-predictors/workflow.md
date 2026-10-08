# Workflow & Project Plan

**Team (2 members):** [Name 1] (**A**) · [Name 2] (**B**)
Because we are two, roles overlap: **A** leads data/EDA/dashboard, **B** leads modelling/interpretation. Every ticket has a *reviewer* (the other person) – nobody merges their own PR.

## 1. Git Workflow
- `main` is protected: changes only via reviewed Pull Request.
- One branch per ticket: `feature/1.2-missing-values-eda`, `fix/...`, `docs/...`
- Commit messages: imperative and specific (`Add missing-value heatmap for training features`).
- PR description: what changed · why · how to test · linked ticket.
- Notebooks: `01_exploratory_data_analysis_<author>.ipynb`, `02_data_cleaning_<author>.ipynb`, `03_feature_engineering_<author>.ipynb`, `04_baseline_models_<author>.ipynb` ...
- Reusable code goes in `src/`; notebooks import from it.

## 2. Timeline (9 weeks)
| Week | Focus | Milestone |
|---|---|---|
| 1 | Setup | Repo forked, env works, docs started, hypotheses drafted |
| 2–3 | Sprint 1 – EDA & cleaning | EDA report, cleaned dataset, **pitch #1** |
| 4–5 | Sprint 2 – Features & baselines | Feature set; LogReg / RF / GB with CV |
| 6 | Sprint 2 – Tuning & evaluation | Tuned models, metrics table, **pitch #2** |
| 7–8 | Sprint 3 – Interpretation & dashboard | SHAP/importance, Streamlit app |
| 9 | Wrap-up | Final docs, 5-min final presentation |

## 3. Hypotheses (Sprint 1)
- **H1** Beliefs (effectiveness, side-effect worry) influence vaccination.
- **H2** Demographics (age, education, income) are key drivers.
- **H3** Preventive behaviours correlate with uptake.
- **H4** Risk perception (concern, perceived risk) affects decisions.
- **H5** Vaccination behaviour is correlated across vaccines (labels show ρ≈0.38).
- **H6** Doctor recommendation and health insurance are among the strongest predictors.

## 4. Research Questions
1. Which age groups are most/least likely to be vaccinated?
2. Do gender, education or income affect uptake?
3. Are people with chronic conditions or health workers more likely to vaccinate?
4. Are seasonal-flu vaccinees also likely to get H1N1?
5. Do employment status or household composition correlate with uptake?
6. How much does a doctor's recommendation matter?
7. Do findings differ between the H1N1 and seasonal vaccines?

## 5. Tickets
Effort: Low/Medium/High · Status: Not Started / In Progress / Review / Complete (track on the GitHub Project board)

### Week 1 – Setup (both complete all individual tasks)
| ID | Title | Owner | Effort | Depends on |
|---|---|---|---|---|
| 0.1 | Fork repo, add teammate + mentor as collaborators, set `git config user.name/email` | A | Low | – |
| 0.2 | Folder structure, `.gitignore`, `requirements.txt`, README skeleton | A | Low | 0.1 |
| 0.3 | Set up venv, install requirements, run a test notebook | A + B | Low | 0.2 |
| 0.4 | Download data into `data/`, review data dictionary | A + B | Low | 0.3 |
| 0.5 | Agree on hypotheses & research questions | A + B | Low | – |
| 0.6 | Create GitHub Project board with these tickets | B | Low | 0.1 |

### Sprint 1 – EDA (Weeks 2–3)
| ID | Title | Owner | Effort | Depends on |
|---|---|---|---|---|
| 1.1 | Data quality: dtypes, duplicates, ranges, merge features + labels | A | Medium | 0.4 |
| 1.2 | Missing-value analysis & strategy (incl. missingness vs. target) | A | Medium | 1.1 |
| 1.3 | Target distribution, imbalance, target correlation (H5, RQ4) | B | Low | 1.1 |
| 1.4 | Demographics vs. uptake (H2, RQ1, 2, 5) | A | Medium | 1.2 |
| 1.5 | Opinions & risk perception vs. uptake (H1, H4) | B | Medium | 1.2 |
| 1.6 | Behaviours, doctor recc., health factors vs. uptake (H3, H6, RQ3, 6) | B | Medium | 1.2 |
| 1.7 | Reorganise high-cardinality categoricals (`employment_*`, `hhs_geo_region`) | A | Medium | 1.2 |
| 1.8 | Correlation analysis (Cramér's V / Spearman), multicollinearity | B | Medium | 1.4–1.6 |
| 1.9 | `02_data_cleaning` notebook + `src/cleaning.py` | A | Medium | 1.2, 1.7 |
| 1.10 | EDA report in `reports/` + 5-min pitch #1 | A + B | Medium | all |

### Sprint 2 – Modelling (Weeks 4–6)
| ID | Title | Owner | Effort | Depends on |
|---|---|---|---|---|
| 2.1 | Aggregated scores (preventive behaviour, risk perception) | A | Medium | 1.9 |
| 2.2 | Ordinal encoding (age, income, education) + one-hot for nominal | A | Medium | 1.9 |
| 2.3 | Preprocessing `Pipeline`/`ColumnTransformer` in `src/` | A | Medium | 2.1, 2.2 |
| 2.4 | Baseline Logistic Regression per target, stratified 5-fold CV | B | Medium | 2.3 |
| 2.5 | Random Forest | B | Medium | 2.3 |
| 2.6 | Gradient Boosting (HistGB / XGBoost / LightGBM) | B | Medium | 2.3 |
| 2.7 | Hyperparameter tuning (RandomizedSearchCV) | B | High | 2.4–2.6 |
| 2.8 | Evaluation: ROC AUC, accuracy, precision/recall/F1, confusion matrix, comparison table | A | Medium | 2.7 |
| 2.9 | Experiment log (model, params, CV scores) | A | Low | 2.4 |
| 2.10 | `src/train_model.py`, `processed_data_dictionary.md`, pitch #2 | A + B | Medium | all |
| 2.11 | Optional: ensemble / DrivenData submission | B | Medium | 2.7 |

### Sprint 3 – Insights & Deployment (Weeks 7–9)
| ID | Title | Owner | Effort | Depends on |
|---|---|---|---|---|
| 3.1 | Feature importance (model-based + permutation), both targets | B | Medium | 2.7 |
| 3.2 | SHAP analysis, non-linearity & interactions | B | High | 3.1 |
| 3.3 | Compare insights across models; relate back to H1–H6 | A + B | Medium | 3.2 |
| 3.4 | Limitations: what model/data can't explain, biases, ethics | A + B | Medium | 3.3 |
| 3.5 | Streamlit dashboard (optional: EDA charts, metrics, prediction demo) | A | High | 2.10 |
| 3.6 | Public-health recommendations | A + B | Medium | 3.3 |
| 3.7 | Final README, docs cleanup, 5-min final presentation | A + B | Medium | all |

## 6. Ticket Template
```
## Ticket ID:
### Title:
### Description:
### Acceptance Criteria:
- 
### Assigned To:
### Reviewer:
### Estimated Effort: [Low/Medium/High]
### Status: [Not Started/In Progress/Review/Complete]
### Dependencies:
```

## 7. Sprint Retrospectives
**Sprint 1** – went well / to improve / challenges: _TBD_
**Sprint 2:** _TBD_
**Sprint 3:** _TBD_

## 8. Decision Log
| Date | Decision | Reason |
|---|---|---|
| | | |

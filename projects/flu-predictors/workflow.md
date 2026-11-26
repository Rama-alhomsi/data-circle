# Workflow & Project Plan

**Author:** Rama Alhomsi. Uyazi Dube worked on Sprint 1 (data cleaning) and left the project afterwards, so Sprints 2 and 3 are done by one person.
Every pull request is reviewed by the mentor or a peer from the Data Circle when possible; otherwise Rama reviews her own PR with the checklist in section 1 before merging.
Status values: Not Started / In Progress / Review / Complete. Track them on the GitHub issues and Project board.

## 1. Git workflow
- `main` is protected: changes only via a Pull Request. Before merging your own PR: read the diff on GitHub, run the notebook top to bottom, and check that no data or model files are included.
- One branch per ticket: `feature/1.2-missing-values`, `fix/...`, `docs/...`
- Commit messages are short and specific (`Add missing-value chart for training features`).
- PR description: what changed, why, how to test, linked ticket (`Closes #<issue>`).
- Notebooks are numbered: `01_exploratory_data_analysis`, `02_data_cleaning_rama_uyazi`, `03_hypothesis_testing_rama`, `04_feature_engineering_rama`, `05_baseline_models_rama`, `06_tuning_and_evaluation_rama`.
- Reusable code goes in `src/`; notebooks import from it. Data files and trained models are never committed.

## 2. Timeline (9 weeks)
| Week | Focus | Milestone |
|---|---|---|
| 1 | Setup | Repo forked, environment works, docs started |
| 2-3 | Sprint 1: EDA and cleaning | EDA report, cleaned dataset, pitch 1 |
| 4-5 | Sprint 2: features and baseline models | Feature set; logistic regression, random forest, gradient boosting with CV |
| 6 | Sprint 2: tuning and evaluation | Tuned models, metrics table, pitch 2 |
| 7-8 | Sprint 3: interpretation and dashboard | Feature importance, Streamlit app |
| 9 | Wrap-up | Final docs, 5-minute presentation |

## 3. Hypotheses
- **H1** Beliefs (effectiveness, side-effect worry) influence vaccination.
- **H2** Demographics (age, education, income) are key drivers.
- **H3** Preventive behaviours correlate with uptake.
- **H4** Risk perception (concern, perceived risk) affects decisions.
- **H5** Vaccination behaviour is correlated across vaccines.
- **H6** Doctor recommendation and health insurance are among the strongest predictors.

Results are in `reports/eda_report.md`.

## 4. Research questions
1. Which age groups are most or least likely to be vaccinated?
2. Do gender, education or income affect uptake?
3. Are people with chronic conditions or health workers more likely to vaccinate?
4. Are seasonal-flu vaccinees also likely to get H1N1?
5. Do employment status or household composition correlate with uptake?
6. How much does a doctor's recommendation matter?
7. Do findings differ between the H1N1 and seasonal vaccines?

## 5. Tickets

### Week 1: Setup
| ID | Title | Owner | Reviewer | Depends on | Status |
|---|---|---|---|---|---|
| 0.1 | Fork repo, add teammate and mentor, set `git config` | Rama | Uyazi | - | Complete |
| 0.2 | Folder structure, `.gitignore`, `requirements.txt`, README skeleton | Rama | Uyazi | 0.1 | Complete |
| 0.3 | Set up venv, install requirements, run a test notebook | Rama + Uyazi | Each other | 0.2 | Complete |
| 0.4 | Download data into `data/`, review the data dictionary | Rama + Uyazi | Each other | 0.3 | Complete |
| 0.5 | Agree on hypotheses and research questions | Rama + Uyazi | Each other | - | Complete |
| 0.6 | Create GitHub Project board with these tickets | Rama + Uyazi | Each other | 0.1 | Complete |

### Sprint 1: EDA (weeks 2-3)
| ID | Title | Owner | Reviewer | Depends on | Status |
|---|---|---|---|---|---|
| 1.1 | Data quality: types, duplicates, ranges, merge features and labels | Rama | Uyazi | 0.4 | Complete |
| 1.2 | Missing-value analysis and strategy (including missingness vs. target) | Rama | Uyazi | 1.1 | Complete |
| 1.3 | Target distribution, imbalance, target correlation (H5, RQ4) | Rama | Uyazi | 1.1 | Complete |
| 1.4 | Demographics vs. uptake (H2, RQ1, 2, 5) | Rama | Uyazi | 1.2 | Complete |
| 1.5 | Opinions and risk perception vs. uptake (H1, H4) | Rama | Uyazi | 1.2 | Complete |
| 1.6 | Behaviours, doctor recommendation, health factors vs. uptake (H3, H6, RQ3, 6) | Rama | Uyazi | 1.2 | Complete |
| 1.7 | Reorganise high-cardinality categoricals (`employment_*`, `hhs_geo_region`) | Rama | Uyazi | 1.2 | Complete |
| 1.8 | Correlation analysis (Cramér's V / Spearman), multicollinearity | Rama | Uyazi | 1.4-1.6 | Complete |
| 1.9 | Data cleaning notebook and `src/cleaning.py` (merged from both notebooks) | Uyazi + Rama | Each other | 1.2, 1.7 | Complete |
| 1.10 | EDA report in `reports/` and 5-minute pitch 1 | Rama + Uyazi | Each other | all | Review |

### Sprint 2: Modelling (weeks 4-6)
| ID | Title | Owner | Reviewer | Depends on | Status |
|---|---|---|---|---|---|
| 2.1 | Aggregated scores (preventive behaviour, risk perception) | Rama | Mentor or peer | 1.9 | In Progress |
| 2.2 | Ordinal encoding (age, education, income) and one-hot for nominal columns | Rama | Mentor or peer | 1.9 | In Progress |
| 2.3 | Preprocessing `Pipeline` / `ColumnTransformer` in `src/` | Rama | Mentor or peer | 2.1, 2.2 | In Progress |
| 2.4 | Baseline logistic regression per target, stratified 5-fold CV | Rama | Mentor or peer | 2.3 | In Progress |
| 2.5 | Random forest | Rama | Mentor or peer | 2.3 | In Progress |
| 2.6 | Gradient boosting (scikit-learn HistGradientBoosting) | Rama | Mentor or peer | 2.3 | In Progress |
| 2.7 | Hyperparameter tuning (RandomizedSearchCV) | Rama | Mentor or peer | 2.4-2.6 | In Progress |
| 2.8 | Evaluation: ROC AUC, accuracy, precision, recall, F1, confusion matrix, comparison table | Rama | Mentor or peer | 2.7 | In Progress |
| 2.9 | Experiment log (model, parameters, CV scores) in `reports/model_results.json` | Rama | Mentor or peer | 2.4 | In Progress |
| 2.10 | `src/train_model.py`, `processed_data_dictionary.md`, modelling decisions, pitch 2 | Rama | Mentor or peer | all | In Progress |
| 2.11 | Optional: ensemble, XGBoost comparison, DrivenData submission | Rama | Mentor or peer | 2.7 | Not Started |

### Sprint 3: Insights and deployment (weeks 7-9)
| ID | Title | Owner | Reviewer | Depends on | Status |
|---|---|---|---|---|---|
| 3.1 | Feature importance (model-based and permutation), both targets | Rama | Mentor or peer | 2.7 | Not Started |
| 3.2 | Non-linearity and interactions (SHAP if feasible) | Rama | Mentor or peer | 3.1 | Not Started |
| 3.3 | Compare insights across models; relate back to H1-H6 | Rama | Mentor or peer | 3.2 | Not Started |
| 3.4 | Limitations: what the model and data cannot explain, biases, ethics | Rama | Mentor or peer | 3.3 | Not Started |
| 3.5 | Streamlit dashboard (optional: EDA charts, metrics, prediction demo) | Rama | Mentor or peer | 2.10 | Not Started |
| 3.6 | Public-health recommendations | Rama | Mentor or peer | 3.3 | Not Started |
| 3.7 | Final README, docs cleanup, 5-minute final presentation | Rama | Mentor or peer | all | Not Started |

## 6. Ticket template
```
## Ticket ID:
### Title:
### Description:
### Acceptance Criteria:
- 
### Assigned To:
### Reviewer:
### Status: [Not Started/In Progress/Review/Complete]
### Dependencies:
```

## 7. Sprint retrospectives (draft: edit before the final pitch)
### Sprint 1
- **Went well:** two independent cleaning notebooks reached the same result and were merged into one shared module; hypothesis tests gave clear evidence; every step is reproducible from the notebooks.
- **To improve:** keep one terminal for Git commands; use `git status` before every commit; protect `main` so an accidental delete cannot land there; agree on names and conventions (labels, file names) before writing code.
- **Challenges:** the teammate left after Sprint 1, so the work was reorganised for one person; an accidental deletion on GitHub was restored with a revert; Jupyter kernel setup in VS Code; `.DS_Store` and data files nearly committed.

### Sprint 2
_To be written at the end of the sprint._

### Sprint 3
_To be written at the end of the sprint._

## 8. Decision log
| Sprint | Decision | Reason |
|---|---|---|
| 1 | Flag columns with more than 5 % missing (plus `household_*`) before filling | Missing answers are related to vaccination |
| 1 | No guessed value for `health_insurance` | 46 % missing and not explained by income or employment |
| 1 | `Not employed` / `Missing` labels | One clear naming convention |
| 1 | Job codes with fewer than 100 people become `Other` | Tiny groups are unreliable; larger rare groups are kept because they can differ a lot |
| 1 | Cleaning rules and learned levels come from the training set only | The test set must be treated like new data |
| 2 | Fill numeric gaps inside the Pipeline (median) | Re-learned in each CV fold, no leakage |
| 2 | One model per target | The two vaccines depend on different factors (age, effectiveness) |
| 2 | Do not use one vaccine as a feature for the other | Leakage: the other target is not known for new people |
| 2 | scikit-learn HistGradientBoosting instead of XGBoost | See `reports/modelling_decisions.md` |
| 2 | ROC AUC as the main metric | Competition metric; independent of the class imbalance |
| 2 | Also report a single 80/20 hold-out split (`src/holdout_check.py`) | Easy to explain to a non-technical audience; agrees with the 5-fold CV |
| 2 | Continue alone after Sprint 1 | Teammate left; Sprint 3 core items first, dashboard optional |

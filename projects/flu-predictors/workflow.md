# Workflow & Project Plan

**Project:** Flu Shot Learning: Predicting Vaccination Patterns
**Team:** Rama Alhomsi (A) and Uyazi Dube (B)
**Project Duration:** 9 weeks

Since our team has two members, responsibilities may overlap. **Member A** leads data analysis, exploratory data analysis (EDA), and dashboard development. **Member B** leads modelling and interpretation. Each ticket must have a reviewer—the other team member. Neither member may merge their own pull request (PR).

## 1. Git Workflow

* Protect the `main` branch. All changes must be submitted through reviewed pull requests.

* Create one branch per ticket, using descriptive names such as `feature/1.2-missing-values-eda`, `fix/...`, or `docs/...`.

* Write clear, specific commit messages using the imperative form, such as `Add missing-value heatmap for training features`.

* Every PR description must explain what changed, why it changed, how to test it, and which ticket it addresses.

* Use consistent notebook naming conventions, such as `01_exploratory_data_analysis_<author>.ipynb`, `02_data_cleaning_<author>.ipynb`, `03_feature_engineering_<author>.ipynb`, and `04_baseline_models_<author>.ipynb`.

* Store reusable functions and modules in `src/` and import them into notebooks.

## 2. Timeline (9 Weeks)

| Week | Focus                                             | Milestone                                                                        |
| ---- | ------------------------------------------------- | -------------------------------------------------------------------------------- |
| 1    | Project setup                                     | Repository and environment configured; documentation started; hypotheses drafted |
| 2–3  | Sprint 1: EDA and data cleaning                   | EDA report, data-cleaning strategy, and Pitch #1                                 |
| 4–5  | Sprint 2: Feature engineering and baseline models | Feature set and baseline models with cross-validation                            |
| 6    | Sprint 2: Tuning and evaluation                   | Tuned models, evaluation metrics, and Pitch #2                                   |
| 7–8  | Sprint 3: Interpretation and dashboard            | Feature-importance analysis, model interpretation, and Streamlit dashboard       |
| 9    | Project wrap-up                                   | Final documentation and five-minute presentation                                 |

## 3. Research Hypotheses (Sprint 1)

* **H1:** Beliefs about vaccine effectiveness and concerns about side effects influence vaccination decisions.

* **H2:** Demographic characteristics, including age, education, and income, are associated with vaccination uptake.

* **H3:** Preventive health behaviours are associated with vaccination uptake.

* **H4:** Risk perception, including health concerns and perceived susceptibility, influences vaccination decisions.

* **H5:** Uptake of seasonal influenza and H1N1 vaccines is positively correlated. The initial analysis suggests a correlation of approximately 0.38; this must be verified using the data.

* **H6:** Doctor recommendations and health insurance status are potentially important predictors of vaccination uptake.

## 4. Research Questions

1. Which age groups are most and least likely to receive vaccinations?

2. Are gender, education, and income associated with vaccination uptake?

3. Are people with chronic health conditions or those working in healthcare more likely to get vaccinated?

4. Are people vaccinated against seasonal influenza also more likely to receive the H1N1 vaccine?

5. Are employment status and household composition associated with vaccination uptake?

6. How strongly is a doctor's recommendation associated with vaccination decisions?

7. Do the findings differ between H1N1 and seasonal influenza vaccination?

## 5. Project Tickets

**Effort levels:** Low, Medium, High
**Status options:** Not Started, In Progress, In Review, Complete

Track all tickets using the GitHub Projects board. Assign each ticket an owner, a reviewer, and any relevant dependencies.

### Week 1 — Project Setup

| ID  | Task                                                                                                                                | Owner | Dependencies |
| --- | ----------------------------------------------------------------------------------------------------------------------------------- | ----- | ------------ |
| 0.1 | Fork the repository, add the teammate and mentor as collaborators, and configure `git config user.name` and `git config user.email` | A     | None         |
| 0.2 | Create the folder structure, `.gitignore`, `requirements.txt`, and README skeleton                                                  | A     | 0.1          |
| 0.3 | Set up the virtual environment, install dependencies, and run a test notebook                                                       | A     | 0.2          |
| 0.4 | Download the datasets into `data/` and review the data dictionary                                                                   | A     | 0.3          |
| 0.5 | Agree on the research hypotheses and questions                                                                                      | A + B | None         |
| 0.6 | Create the GitHub Projects board and add the tickets                                                                                | A + B | 0.1          |

### Sprint 1 — Exploratory Data Analysis (Weeks 2–3)

| ID   | Task                                                                                                                                                  | Owner | Dependencies |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------------ |
| 1.1  | Assess data quality: data types, duplicates, value ranges, and merging features with labels                                                           | A     | 0.4          |
| 1.2  | Analyse missing values and define a handling strategy, including missingness in relation to the targets                                               | A     | 1.1          |
| 1.3  | Examine target distributions, class imbalance, and correlation between vaccination targets (H5, RQ4)                                                  | A     | 1.1          |
| 1.4  | Analyse demographic characteristics in relation to vaccination uptake (H2, RQ1, RQ2, RQ5)                                                             | A     | 1.2          |
| 1.5  | Analyse opinions and risk perceptions in relation to vaccination uptake (H1, H4)                                                                      | A     | 1.2          |
| 1.6  | Analyse preventive behaviours, doctor recommendations, and health factors in relation to vaccination uptake (H3, H6, RQ3, RQ6)                        | A     | 1.2          |
| 1.7  | Investigate and appropriately handle high-cardinality categorical features, including `employment_*` and `hhs_geo_region`                             | A     | 1.2          |
| 1.8  | Conduct association analysis using appropriate measures, such as Cramér's V and Spearman's correlation, and assess multicollinearity where applicable | A     | 1.4–1.6      |
| 1.9  | Create the `02_data_cleaning` notebook and implement reusable cleaning functions in `src/cleaning.py`                                                 | B     | 1.2, 1.7     |
| 1.10 | Prepare the EDA report in `reports/` and deliver the five-minute Pitch #1                                                                             | A + B | 1.1–1.9      |

### Sprint 2 — Feature Engineering and Modelling (Weeks 4–6)

| ID   | Task                                                                                                                              | Owner | Dependencies |
| ---- | --------------------------------------------------------------------------------------------------------------------------------- | ----- | ------------ |
| 2.1  | Create aggregated scores for preventive behaviours and risk perception where justified                                            | A     | 1.9          |
| 2.2  | Apply suitable ordinal encoding to ordered features, such as age, income, and education, and one-hot encoding to nominal features | A     | 1.9          |
| 2.3  | Implement a preprocessing pipeline using `Pipeline` and `ColumnTransformer` in `src/`                                             | A     | 2.1, 2.2     |
| 2.4  | Train baseline Logistic Regression models for both targets using stratified five-fold cross-validation                            | B     | 2.3          |
| 2.5  | Train and evaluate Random Forest models                                                                                           | B     | 2.3          |
| 2.6  | Train and evaluate a Gradient Boosting model, such as HistGradientBoosting, XGBoost, or LightGBM                                  | B     | 2.3          |
| 2.7  | Tune hyperparameters using `RandomizedSearchCV`                                                                                   | B     | 2.4–2.6      |
| 2.8  | Evaluate models using ROC AUC, accuracy, precision, recall, F1-score, and confusion matrices; prepare a comparison table          | A     | 2.4–2.7      |
| 2.9  | Maintain an experiment log containing model names, parameters, and cross-validation scores                                        | A     | 2.4          |
| 2.10 | Create `src/train_model.py`, document the processed dataset in `processed_data_dictionary.md`, and prepare Pitch #2               | A + B | 2.1–2.9      |
| 2.11 | Optional: experiment with an ensemble or prepare a DrivenData competition submission                                              | B     | 2.7          |

### Sprint 3 — Insights and Deployment (Weeks 7–9)

| ID  | Task                                                                                                               | Owner | Dependencies       |
| --- | ------------------------------------------------------------------------------------------------------------------ | ----- | ------------------ |
| 3.1 | Analyse feature importance using model-based and permutation methods for both targets                              | B     | 2.7                |
| 3.2 | Conduct SHAP analysis to investigate nonlinear relationships and feature interactions, where appropriate           | B     | 3.1                |
| 3.3 | Compare findings across models and relate the results to hypotheses H1–H6                                          | A + B | 3.2                |
| 3.4 | Document limitations, potential biases, ethical considerations, and aspects that the data or models cannot explain | A + B | 3.3                |
| 3.5 | Optional: develop a Streamlit dashboard featuring EDA charts, model metrics, and a prediction demonstration        | A     | 2.10               |
| 3.6 | Develop evidence-based public health recommendations based on the findings                                         | A + B | 3.3                |
| 3.7 | Finalise the README and documentation and prepare the five-minute final presentation                               | A + B | All relevant tasks |

## 6. Ticket Template

Use the following template for each GitHub issue:

```
## Ticket ID:
## Title:

### Description
Describe the task and its purpose.

### Acceptance Criteria
- [ ] The task is completed.
- [ ] The results are documented.
- [ ] The code or notebook has been tested.
- [ ] A pull request has been reviewed and approved.

### Assigned To:
### Reviewer:
### Effort: Low / Medium / High
### Status: Not Started / In Progress / In Review / Complete
### Dependencies:
### Related Hypothesis or Research Question:
```

## 7. Sprint Retrospectives

After each sprint, both team members should discuss what went well, what could be improved, and which challenges they encountered.

* **Sprint 1:** What went well / What could be improved / Challenges

* **Sprint 2:** What went well / What could be improved / Challenges

* **Sprint 3:** What went well / What could be improved / Challenges

Record the outcomes and agreed actions in the project documentation.


---

**Important project note:** The project investigates associations and predictive relationships, not necessarily causal effects. Any conclusions about vaccination behaviour should reflect this limitation. Confirm the reported target correlation and other initial assumptions during EDA before presenting them as findings.

# Flu Predictors: Predicting Vaccination Patterns

> Team: **[Name 1]** & **[Name 2]** · Course/Program: **[School / Course]** · Mentor: **[Name]**

## 1. Objective
Predict whether respondents of the 2009 National H1N1 Flu Survey (NHFS, CDC) received the
**H1N1 vaccine** and the **seasonal flu vaccine**, and identify which demographic, behavioural
and opinion factors most strongly influence vaccination decisions. Findings are intended to
inform public-health communication strategies.

- Task: two binary classification targets (`h1n1_vaccine`, `seasonal_vaccine`)
- Metric: mean ROC AUC across both targets
- Source: [DrivenData – Flu Shot Learning](https://www.drivendata.org/competitions/66/flu-predictors/)

## 2. Repository Structure
```
├── data/            # data_dictionary.md, processed_data_dictionary.md (CSVs are git-ignored)
├── notebooks/       # numbered, author-tagged notebooks (01_exploratory_data_analysis_<author>.ipynb)
├── reports/         # written reports and presentation slides
├── src/             # reusable Python modules (cleaning, features, train_model.py)
├── requirements.txt
├── workflow.md      # sprint plan, tickets, decisions log
└── README.md
```

## 3. Setup
```bash
git clone https://github.com/<org-or-user>/flu-predictors.git
cd flu-predictors
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
Download the four CSV files from DrivenData into `data/` (see `data/data_dictionary.md`):
`training_set_features.csv`, `training_set_labels.csv`, `test_set_features.csv`, `submission_format.csv`.

## 4. How to Reproduce
1. Run notebooks in numeric order (`01_...` → `0N_...`).
2. Reusable logic lives in `src/`; notebooks import from it.
3. Train final models: `python src/train_model.py` *(added in Sprint 2)*.
4. Launch dashboard: `streamlit run src/app.py` *(added in Sprint 3)*.

## 5. Key Findings
*To be completed at the end of each sprint.*

| Sprint | Summary |
|---|---|
| 1 – EDA | _TBD_ |
| 2 – Modelling | _TBD_ (CV ROC AUC: H1N1 = _, Seasonal = _) |
| 3 – Insights | _TBD_ |

## 6. Ethics & Data Use
Per CDC guidelines the data is used for statistical analysis only; we do not attempt to identify
individuals or link the data with other identifiable datasets. Survey data may carry
non-response and self-report bias (see reports for discussion).

## 7. Contributors
| Name | Role |
|---|---|
| [Name 1] | Data preprocessing & EDA lead; dashboard |
| [Name 2] | Modelling lead; interpretation |

# Flu Shot Learning: Predicting Vaccination Patterns

A data science project exploring factors associated with H1N1 and seasonal influenza vaccination using the CDC's 2009 National H1N1 Flu Survey (NHFS).

## Project Overview

The goal of this project is to investigate vaccination patterns and identify factors associated with whether individuals received:

- **H1N1 vaccine** (`h1n1_vaccine`)
- **Seasonal flu vaccine** (`seasonal_vaccine`)

The project combines exploratory data analysis, data preparation, statistical hypothesis testing, and machine learning to understand vaccination behaviour and develop predictive models.

## Objectives

- Explore demographic, behavioural, and opinion-related factors associated with vaccination.
- Investigate relationships between explanatory variables and vaccination outcomes.
- Apply statistical methods to test hypotheses and measure associations.
- Develop and evaluate classification models for both vaccination targets.
- Interpret findings using statistical analysis and data visualisation.

## Dataset

The project uses the [Flu Shot Learning dataset from DrivenData](https://www.drivendata.org/competitions/66/flu-predictors/), based on the CDC's 2009 National H1N1 Flu Survey.

The dataset contains survey responses and two binary target variables representing H1N1 and seasonal flu vaccination.

Raw data files are not included in this repository and must be downloaded separately.

## Project Workflow

1. **Exploratory Data Analysis (EDA):** Examine the dataset, distributions, missing values, and potential relationships.
2. **Data Cleaning and Preparation:** Handle missing values, prepare features, and organise the data for analysis.
3. **Statistical Hypothesis Testing:** Investigate associations between selected variables and vaccination outcomes.
4. **Machine Learning:** Develop classification models and evaluate their predictive performance.
5. **Interpretation:** Analyse model performance, identify important features, and communicate findings.

## Repository Structure

```text
data-circle/
├── README.md
├── flu_shot_predictors_sprint1.pptx
└── projects/
    └── flu-predictors/
        ├── data/
        │   ├── data_dictionary.md
        │   └── processed_data_dictionary.md
        ├── notebooks/
        │   ├── 01_exploratory_data_analysis_rama.ipynb
        │   ├── 02_data_cleaning_rama_uyazi.ipynb
        │   └── 03_hypothesis_testing_rama.ipynb
        ├── src/
        │   ├── cleaning.py
        │   └── hypothesis.py
        ├── requirements.txt
        ├── workflow.md
        └── README.md
```

The machine learning notebook is being developed and reviewed separately before being integrated into the main branch.

## Technologies and Tools

- **Python**
- **Pandas and NumPy** – data manipulation and numerical analysis
- **SciPy** – statistical testing
- **Scikit-learn** – machine learning and model evaluation
- **Matplotlib and Seaborn** – data visualisation
- **Jupyter Notebook** – exploratory and statistical analysis
- **Git and GitHub** – version control

## Evaluation

The project follows the DrivenData competition evaluation metric: the mean ROC AUC across the two vaccination targets.

Model performance and statistical findings will be documented after validation and evaluation.

## Limitations

- The survey data is observational and based on self-reported responses.
- Missing values and non-response may affect the analysis.
- Statistical associations do not establish causation.
- The exploratory statistical calculations do not account for the complex survey design unless explicitly stated.

## Project Status

| Component | Status |
|---|---|
| Exploratory Data Analysis | Available |
| Data Cleaning and Preparation | Available |
| Statistical Hypothesis Testing | Available |
| Machine Learning | In progress |
| Model Evaluation and Interpretation | In progress |

## Data Source

[DrivenData – Flu Shot Learning: Predicting H1N1 and Seasonal Flu Vaccines](https://www.drivendata.org/competitions/66/flu-predictors/)


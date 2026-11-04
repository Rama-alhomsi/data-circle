# Flu Shot Learning: Predicting Vaccination Patterns

## Project Overview

This project investigates factors associated with H1N1 and seasonal influenza vaccination uptake using data from the 2009 National H1N1 Flu Survey (NHFS), provided through the DrivenData Flu Shot Learning challenge.

The objective is to understand vaccination patterns, identify relevant demographic and behavioural factors, and prepare the dataset for future predictive modelling.

## Research Questions

- Which demographic and socioeconomic characteristics are associated with vaccination uptake?
- How are health behaviours and opinions related to vaccination decisions?
- What role does a doctor's recommendation play in vaccination uptake?
- Are the factors associated with H1N1 vaccination similar to those associated with seasonal influenza vaccination?

## Dataset

The dataset contains survey responses from 26,707 respondents.

The two target variables are:

- `h1n1_vaccine`: Whether the respondent received the H1N1 vaccine.
- `seasonal_vaccine`: Whether the respondent received the seasonal influenza vaccine.

The dataset includes demographic information, health-related characteristics, opinions, and behavioural indicators.

**Data source:** [DrivenData – Flu Shot Learning](https://www.drivendata.org/competitions/66/flu-shot-learning/)

The original survey data is not included in this repository. Download the competition data and place the relevant CSV files in the project's `data/` directory.

## Project Structure

```text
flu-predictors/
│
├── data/
│   ├── data_dictionary.md
│   └── processed_data_dictionary.md
│
├── notebooks/
│   ├── 01_exploratory_data_analysis_rama.ipynb
│   ├── 02_data_cleaning_rama_uyazi.ipynb
│   └── 03_hypothesis_testing_rama.ipynb
│
├── reports/
│
├── src/
│   ├── cleaning.py
│   └── hypothesis.py
│
├── requirements.txt
├── workflow.md
└── README.md
```

## Project Workflow

### 1. Exploratory Data Analysis (EDA)

- Examined dataset structure and variable distributions.
- Investigated missing values and potential data-quality issues.
- Explored relationships between demographic, behavioural, and health-related variables.
- Compared vaccination uptake across different respondent groups.

### 2. Data Cleaning and Preparation

- Checked duplicate records and respondent identifiers.
- Investigated missingness patterns and their relationship with vaccination outcomes.
- Distinguished between missing information and meaningful categories.
- Applied data preparation and imputation strategies.
- Ensured consistent feature columns between training and test datasets.
- Avoided data leakage by learning relevant preprocessing values from training data.

### 3. Hypothesis Testing

Investigated relationships between vaccination outcomes and selected survey variables using:

- Chi-square tests.
- Cramér's V.
- Spearman correlation.
- Confidence intervals.
- Odds ratios.

The analysis also considered potential confounding factors and the limitations of interpreting observational survey data.

### 4. Predictive Modelling

Predictive modelling is a planned next stage. The prepared dataset will be used to develop and evaluate classification models for both vaccination outcomes.

## Technologies

- Python
- pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Jupyter Notebook
- Git and GitHub

## Key Analytical Insights

The hypothesis-testing analysis identified several associations worth investigating further:

- Doctor recommendations were strongly associated with both H1N1 and seasonal vaccination uptake.
- H1N1 and seasonal vaccination decisions were positively associated.
- Age showed an association with seasonal vaccination.
- Preventive health behaviours showed a positive relationship with H1N1 vaccination, although the observed correlation was relatively weak.

These findings describe associations in observational survey data and should not be interpreted as evidence of causation.

## Limitations

- The dataset is based on self-reported survey responses.
- Missing information may introduce bias.
- Observed associations do not establish causal relationships.
- The survey reflects vaccination patterns in 2009 and may not represent current behaviour.

## Project Status

<ins>Completed</ins>
- Exploratory data analysis.
- Data cleaning and preparation.
- Initial hypothesis testing.

<ins>In Progress / Planned</ins>
- Further feature engineering.
- Predictive modelling.
- Model evaluation and comparison.
- Final presentation of results.


**Project focus:** Understanding vaccination patterns through data analysis and statistical investigation.

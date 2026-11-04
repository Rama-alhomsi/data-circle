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

The following dataset files are included in the repository's `data/` directory:

- `training_set_features.csv`
- `training_set_labels.csv`
- `test_set_features.csv`
- `submission_format.csv`
- `data_dictionary.md`
- `processed_data_dictionary.md`

## Project Structure

```text
flu-predictors/
│
├── data/
│   ├── training_set_features.csv
│   ├── training_set_labels.csv
│   ├── test_set_features.csv
│   ├── submission_format.csv
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
│   ├── README.md
│   ├── __init__.py
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

Implemented reusable preprocessing functions in `src/cleaning.py` and applied them to the training and test datasets.

The preparation process includes:

- Standardizing text values and categorical labels.
- Investigating missing values and creating missing-value indicators.
- Distinguishing structurally inapplicable employment information from genuinely missing responses.
- Grouping infrequent employment categories using thresholds learned from the training data.
- Creating ordinal representations of age, education, and income categories.
- Applying numeric mode imputation using values learned from the training dataset.
- Validating respondent identifiers, value ranges, missing values, row counts, and target integrity.
- Applying consistent preprocessing rules to training and test datasets.

**Validation results:**

- Prepared 26,707 training records and 26,708 test records.
- Confirmed that respondent IDs are unique.
- Confirmed that no missing values remain after preprocessing.
- Confirmed that training and test datasets have matching feature columns.
- Confirmed that vaccination target values and overall vaccination rates remain unchanged after cleaning.

The preprocessing functions are reusable and keep training-derived information separate from test-data preparation. Fold-specific imputation within a scikit-learn pipeline is planned for the predictive modelling stage.

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

Additional libraries listed in `requirements.txt` support planned modelling and dashboard development.

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

**Completed**
- Exploratory data analysis.
- Data cleaning and preparation.
- Initial hypothesis testing.

**In Progress / Planned**
- Further feature engineering.
- Predictive modelling.
- Model evaluation and comparison.
- Final presentation of results.

For more details about project tasks and collaboration, see [`workflow.md`](workflow.md).

## Installation

Clone the repository:

```bash
git clone https://github.com/Rama-alhomsi/data-circle.git
```

Navigate to the project directory:

```bash
cd data-circle/projects/flu-predictors
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

**Project focus:** Understanding vaccination patterns through data analysis and statistical investigation.
- Further feature engineering.
- Predictive modelling.
- Model evaluation and comparison.
- Final presentation of results.


**Project focus:** Understanding vaccination patterns through data analysis and statistical investigation.

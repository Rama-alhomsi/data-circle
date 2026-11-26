# Sprint 1 Report: Exploratory Data Analysis

**Author:** Rama Alhomsi (data cleaning with Uyazi Dube, Sprint 1) · **Project:** Flu Predictors · **Data:** National 2009 H1N1 Flu Survey (CDC)

Notebooks: `01_exploratory_data_analysis_rama`, `02_data_cleaning_rama_uyazi`, `03_hypothesis_testing_rama`.
All numbers below come from the training data (26,707 respondents) and can be reproduced by running these notebooks.

## 1. Goal and data
We want to predict whether a person received the **H1N1 vaccine** and the **seasonal flu vaccine**, and to understand which factors are associated with the decision, so that vaccination campaigns can be targeted better.

- 26,707 respondents, 35 questions: opinions, behaviours, health and access, demographics.
- Two targets: `h1n1_vaccine` (about **21 %** vaccinated) and `seasonal_vaccine` (about **47 %**). The classes are imbalanced, so we use stratified cross-validation and ROC AUC.
- The respondent id is unique and there are no duplicate answer rows. Both targets are complete, so no rows were removed.

## 2. Hypotheses
| ID | Hypothesis |
|---|---|
| H1 | Beliefs (effectiveness, worry about side effects) influence vaccination |
| H2 | Demographics (age, education, income) are key drivers |
| H3 | Preventive behaviours correlate with uptake |
| H4 | Risk perception (concern, perceived risk) affects decisions |
| H5 | Vaccination behaviour is correlated across the two vaccines |
| H6 | A doctor's recommendation and health insurance are among the strongest predictors |

## 3. Data cleaning (tickets 1.1, 1.2, 1.7, 1.9)
| Problem | Finding | Decision |
|---|---|---|
| Missing answers | `health_insurance` is 46 % missing; H1N1 uptake is **11 %** for people who skipped it vs **30 %** for those who answered | Add a `_missing` flag for every column with more than 5 % missing (plus `household_*`); do not guess values |
| Job columns | 50 % missing, mostly people who do not work | Label `Not employed`; other gaps `Missing` |
| Many job codes | Small codes can differ strongly (one group of 148 people has 62 % H1N1 uptake) | Only codes with fewer than 100 people become `Other` (threshold learned from the training set) |
| Text labels | `census_msa` contained a double space | Whitespace stripped (`tidy_text`) |
| Ordinal columns | Age, education and income have an order | Added `age_group_ord`, `education_ord`, `income_ord` |
| Numeric gaps | 0.1 to 8 % | Filled inside the model Pipeline, learned from the training folds only |

The cleaning lives in `src/cleaning.py`, is validated by `validate()`, and is applied to the test set with exactly the same rules. Details of how the two team members' notebooks were merged are in `reports/cleaning_changes.md`.

## 4. Findings
**Which features matter most** (Cramér's V, 0 = no association, 1 = perfect; below 0.1 weak, 0.1 to 0.3 moderate, above 0.3 strong):

| Vaccine | Strongest features |
|---|---|
| H1N1 | Doctor's recommendation (0.40), perceived risk (0.33), perceived effectiveness (0.30) |
| Seasonal | Perceived effectiveness (0.40), perceived risk (0.39), doctor's recommendation (0.36), age (0.29) |

| Hypothesis | Evidence | Verdict |
|---|---|---|
| H1 Beliefs | Perceived effectiveness: Spearman ρ = 0.29 (H1N1), 0.40 (seasonal). "Worry about getting sick from the vaccine" is close to 0 | Supported |
| H2 Demographics | Only age matters, and only for seasonal flu (V = 0.29; for H1N1 0.05). Sex, race, education, income: V at most 0.11 | Partly supported |
| H3 Behaviours | Behaviour score ρ = 0.08 (H1N1), 0.12 (seasonal) | Weak |
| H4 Risk perception | Perceived risk ρ = 0.31 (H1N1), 0.39 (seasonal) | Supported |
| H5 Cross-vaccine | Odds ratio 8.3 (95 % CI 7.7 to 8.9); 38 % of seasonal-vaccine takers also got H1N1 vs 7 % of the others | Strongly supported |
| H6 Doctor / insurance | Recommendation: +40 percentage points for both vaccines. Insurance: +17 (H1N1) and +31 (seasonal) | Supported for the doctor, partly for insurance |

**Answers to our research questions**
1. **Age:** seasonal uptake rises from 28 % (18 to 34) to 67 % (65+). For H1N1 it stays between about 19 % and 24 %.
2. **Gender, education, income:** weak effects (V at most 0.08).
3. **Chronic illness and health workers:** seasonal uptake is 19 points higher with a chronic condition; health workers have 22 points higher H1N1 uptake.
4. **Seasonal and H1N1:** strongly linked (see H5).
5. **Employment and household:** employment looks important (V = 0.16 for seasonal) but is mostly age in disguise: 53 % of people outside the labor force are 65 or older. Inside age groups the effect halves (V about 0.07).
6. **Doctor's recommendation:** the strongest single factor for H1N1.
7. **Differences between vaccines:** age and "perceived effectiveness" matter more for seasonal flu; the doctor's recommendation matters most for H1N1.

## 5. Limitations
- **Associations, not causes.** Doctors tend to recommend the vaccine to older or higher-risk people, so part of the +40 point gap is not the recommendation itself.
- **Reverse causality.** People who were vaccinated may report more trust in the vaccine afterwards.
- **Self-reported survey** from 2009 to 2010; missing data is not random.
- **Confounding** (age and employment) can mislead simple comparisons.
- **Anonymised codes** for industry, occupation and region cannot be interpreted.

## 6. Consequences for Sprint 2
Build a risk-perception score and a behaviour score, a doctor-by-risk interaction, a priority-group indicator and ordered encodings. Use pipelines so no preprocessing leaks information from validation folds. Do not use one vaccine as a feature for the other.

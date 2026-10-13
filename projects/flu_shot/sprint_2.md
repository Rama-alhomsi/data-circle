# Sprint 2: Model Development
**Week 4–6**

### Overview
In this sprint, teams will develop machine learning models to predict both target variables (H1N1 and seasonal flu vaccination). The focus will be on feature engineering, model selection, and optimization.

1. Feature engineering  
- Create aggregated scores (e.g., preventive behavior score, risk perception score)  
- Group demographic variables (e.g., age groups, income levels)  
- Encode ordinal variables appropriately (preserve order when relevant) 
- Create features that reflect your hypothesis  

2. Apply models to explore relationships in the data  
Machine learning is used as a tool to support understanding, rather than only for prediction. The goal is not only to build accurate models, but to generate meaningful insights from them.
- Logistic Regression: interpretable baseline  
- Random Forest: capture non-linear relationships  
- Gradient Boosting: more flexible modelling
- Any other models you would like to try

Optional approaches:  

- Train separate models for `h1n1_vaccine` and `seasonal_vaccine`  
- Compare feature importance across models

When building models, consider structuring your workflow to ensure consistency and reproducibility. This may include:  

- Using **pipelines** to combine preprocessing and modelling steps  
- Applying **cross-validation** to evaluate model performance more robustly  
- Keeping track of experiments and model configurations

3. Evaluate and interpret results
- Accuracy
- F1-score, Precision, Recall  
- Confusion Matrix  
- ROC-AUC 


### Deliverables
- Engineered features and modelling dataset  
- Trained models and comparisons  
- Interpretation of results  
- Reproducible pipeline  
- Pitch-presentation (5-minute presentation of results achieved in this sprint)

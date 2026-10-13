# Flu Shot Learning: Predicting Vaccination Patterns

## Project Overview
In this project, you will develop machine learning models to predict whether individuals received H1N1 and seasonal flu vaccines based on their demographic information, social factors, beliefs, and behaviors. This project addresses a crucial public health challenge: understanding what factors influence vaccination decisions to improve future vaccination campaigns.

## Competition Link
[DrivenData - Flu Shot Learning Competition](https://www.drivendata.org/competitions/66/flu-shot-learning/)


## Project Goals
1. Develop classification models to predict two target variables:
   - Whether a person received the H1N1 vaccine
   - Whether a person received the seasonal flu vaccine
2. Analyze which factors most strongly influence vaccination decisions
3. Create visualizations that effectively communicate your findings
4. Deploy a simple dashboard showcasing your models and insights

## Data Description

### Dataset Source
The data comes from the National 2009 H1N1 Flu Survey (NHFS), conducted by the CDC between October 2009 and June 2010 during the "swine flu" pandemic.

### Features Overview
The dataset contains 36 columns representing:
- Demographic variables (age, income, education, etc.)
- Social indicators (geographic region, household composition)
- Opinions and perceptions about vaccines and disease risk
- Behavioral indicators (preventive health measures taken)

### Target Variables
- **h1n1_vaccine**: Whether the respondent received the H1N1 vaccine (0 = No, 1 = Yes)
- **seasonal_vaccine**: Whether the respondent received the seasonal flu vaccine (0 = No, 1 = Yes)

## Project Structure

### Sprint 1: Exploratory Data Analysis (3 weeks)
- Clean and preprocess the dataset
- Handle missing values and categorical variables
- Visualize patterns and correlations in the data
- Analyze distributions of key variables
- **Deliverable**: EDA report with visualizations and initial insights

### Sprint 2: Model Development (3 weeks)
- Feature engineering and selection
- Train baseline classification models for both target variables
- Implement cross-validation and hyperparameter tuning
- Evaluate models using ROC AUC metric
- **Deliverable**: Trained models with documented performance metrics

### Sprint 3: Insights & Deployment (3 weeks)
- Analyze feature importance and model explanations
- Create a Streamlit dashboard to visualize predictions and insights
- Document findings and recommendations for public health strategies
- **Deliverable**: Interactive dashboard and final presentation

## Technical Requirements

### Required Technologies
- Python (pandas, scikit-learn, matplotlib/seaborn)
- Jupyter Notebooks for exploration and documentation
- GitHub for version control
- Streamlit for dashboard creation

### Performance Metric
- ROC AUC (area under the receiver operating characteristic curve)
- Final score is the average ROC AUC across both prediction targets

## Resources

### Dataset Files
- `training_set.csv`: Training data with labels
- `test_set.csv`: Test data for predictions
- `submission_format.csv`: Template for competition submissions

### Technical Resources
- [Scikit-learn Classification Documentation](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
- [Feature Engineering Techniques](https://scikit-learn.org/stable/modules/preprocessing.html)
- [ROC AUC Scoring](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html)
- [Streamlit Documentation](https://docs.streamlit.io/)

### Domain Resources
- CDC resources on vaccination and public health
- Academic papers on vaccine hesitancy and adoption

## Evaluation Criteria

### Technical Assessment
- Data preprocessing and feature engineering
- Model performance (ROC AUC score) 
- Code quality and documentation 
- Dashboard functionality and design

### Presentation & Communication 
- Clear explanation of methodology
- Quality of insights derived 
- Visualization effectiveness 

## Mentoring Structure
Volunteers will provide consistent guidance throughout the project. Your mentors will:
- Provide technical support during weekly sessions
- Review your code and give specific feedback
- Help troubleshoot challenges
- Guide your analysis toward meaningful insights

## Team Organization
- Teams will consist of 2-3 students
- Each team should designate roles:
  - Data preprocessing lead
  - Modeling specialist
  - Visualization/dashboard developer
  - (Roles can overlap depending on team size)

## Important Notes

### Data Use Restrictions
As per CDC guidelines:
1. Use the data for statistical reporting and analysis only
2. Do not attempt to identify individuals in the dataset
3. Do not link this data with other individually identifiable datasets

### Ethical Considerations
- Consider how your findings might impact public health policy
- Reflect on implications for vaccine hesitancy and health communication
- Discuss potential biases in the data and how they might affect your conclusions

## Extensions for Advanced Students
- Implement ensemble methods combining multiple models
- Develop more advanced feature engineering techniques
- Create a more sophisticated interactive dashboard
- Conduct causal inference analysis on specific features


## Weekly Checkpoints

### Week 1: Project Setup
- Form teams and assign roles
- Set up GitHub repository
- Initial data exploration

### Week 2-3: Data Preprocessing
- Clean data and handle missing values
- Engineer initial features
- Submit EDA report

### Week 4-5: Model Building
- Develop baseline models
- Implement feature selection
- Begin hyperparameter tuning

### Week 6: Model Optimization
- Finalize model tuning
- Evaluate performance
- Submit model documentation

### Week 7-8: Dashboard Development
- Design dashboard interface
- Implement visualizations
- Integrate model predictions

### Week 9: Final Presentation
- Prepare final presentation
- Complete all documentation
- Submit final project

## Acknowledgments
- Data provided by Taarifa and the Tanzania Ministry of Water
- Project taken from the DrivenData competition

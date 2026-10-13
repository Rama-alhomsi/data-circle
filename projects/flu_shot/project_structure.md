# Project Structure 


```
├── data/
│   ├── data_dictionary.md   # Metadata on an initial raw dataset
    ├── processed_data_dictionary.md  # Metadata on data prepared for modelling
│   └── .gitignore           # (Contains: *.csv, *.zip)
├── notebooks/               # Jupyter Notebooks (numbered sequentially)
├── reports/                 # Written report & Presentation slides
├── src/                     # Modular Python scripts
├── requirements.txt         # list of all the specific Python libraries and their versions 
├── workflow.md              # track the development lifecycle
└── README.md                # objective, setup, and key findings

```

Standardize your repository to ensure reproducibility:

* data/: `data_dictionary.md` including download link and a brief description of the features 
* notebooks/: Sequentially numbered research files (`01_exploratory_data_analysis_author.ipynb`, `02_data_cleaning_author.ipynb`, `03_feature_engineering_author.ipynb`, etc.)
* src/: Modular, reusable production code in Python (e.g. `train_model.py`)
* README.md: The project's description (objective, setup, and key findings)

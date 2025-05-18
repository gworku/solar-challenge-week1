# Solar Challenge Week 1 - Comprehensive Analysis

## Project Overview
This project analyzes solar energy potential across three West African countries (Benin, Sierra Leone, and Togo) through:
1. Data cleaning and exploratory analysis
2. Cross-country statistical comparisons
3. Interactive dashboard visualization

## Repository Structure
├── .github/ # CI/CD workflows
│ └── workflows/
│ └── ci.yml # GitHub Actions pipeline
├── app/ # Streamlit dashboard
│ ├── init.py
│ ├── main.py # Dashboard entry point
│ └── utils.py # Data loading helpers
├── data/ # Raw and cleaned data (git-ignored)
├── notebooks/ # Jupyter notebooks
│ ├── benin_eda.ipynb # Benin exploratory analysis
│ ├── sierraleone_eda.ipynb # Sierra Leone analysis
│ ├── togo_eda.ipynb # Togo analysis
│ └── compare_countries.ipynb # Cross-country comparison
└── requirements.txt # Python dependencies

## Detailed Workflow

### Data Processing Pipeline
1. **Data Loading**: 
   - Raw CSV files loaded with pandas
   - Automatic datetime parsing for time series analysis

2. **Data Cleaning**:
   - Missing value imputation (median for numerical columns)
   - Outlier detection using Z-score (threshold = 3σ)
   - Type conversion and validation

3. **Analysis**:
   - Time series decomposition
   - Correlation matrices
   - Statistical distribution fitting
   - Hypothesis testing (ANOVA)

### Dashboard Features
- Interactive country selection
- Multiple visualization types (boxplots, histograms, scatter)
- Dynamic statistical summaries
- Responsive design for different screen sizes

## Setup Instructions

```bash
# 1. Clone repository
git clone https://github.com/yourusername/solar-challenge-week1.git
cd solar-challenge-week1

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch components
jupyter notebook  # For analysis notebooks
streamlit run app/main.py  # For dashboard
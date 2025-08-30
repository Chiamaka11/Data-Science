# Energy Consumption & Biofuel Analysis Project

## Overview
This project analyzes global energy consumption trends, with a focus on biofuel, renewable energy, and fossil fuel usage. It includes data cleaning, exploratory data analysis (EDA), visualization, and predictive modeling to forecast energy consumption for countries based on key features.

The project aims to provide insights into energy trends, greenhouse gas emissions, and the impact of renewable energy adoption.

---

## Features

- **Data Cleaning & Preprocessing**  
  Handling missing values, duplicates, and filtering relevant columns.

- **Exploratory Data Analysis (EDA)**  
  - Trends in energy consumption over years  
  - Top consumers of primary energy  
  - Relationships between GDP, population, and energy consumption  
  - Biofuel adoption analysis

- **Visualizations**  
  - Bar charts, line charts, and scatter plots  
  - Predicted vs actual plots for models  
  - Optional: Tableau / PowerBI dashboards for interactive exploration

- **Predictive Modeling**  
  - Linear Regression  
  - Random Forest Regressor  
  - XGBoost Regressor  

- **Model Interpretability**  
  - SHAP values for feature importance  
  - Residual analysis  
  - Scenario analysis

---

## Dataset

The dataset includes the following columns (non-exhaustive):

- `country`, `year`, `population`, `gdp`  
- `biofuel_consumption`, `renewables_consumption`, `coal_consumption`, `gas_consumption`, `oil_consumption`  
- `electricity_generation`, `electricity_demand`, `carbon_intensity_elec`, `greenhouse_gas_emissions`  

*Data is sourced from publicly available global energy datasets.*

---

## Usage

1. Clone the repository:
```bash
git clone https://github.com/yourusername/your-repo-name.git

pip install -r requirements.txt

jupyter notebook Energy_Analysis.ipynb

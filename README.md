# Airbnb Skopje Data Analysis

## Project Description

This project analyzes Airbnb listings in Skopje, North Macedonia.

The main goal of the project is to collect, clean, process,
analyze and visualize Airbnb data in order to identify
patterns in prices, ratings, reviews, accommodation types
and host characteristics.

The project uses Python and Jupyter Notebook for data analysis
and visualization.

---

## Research Questions

The project investigates the following questions:

1. What is the typical nightly Airbnb price in Skopje?
2. Which accommodation types have the highest average prices?
3. Is there a relationship between price and rating?
4. Do Superhosts have higher ratings than non-Superhosts?
5. Is the number of reviews related to the rating?
6. How does guest capacity affect the price?
7. How do Airbnb prices differ between neighbourhoods?
8. Which listings provide the best combination of price and rating?

---
## How to run the project
### 1. Clone the repository

```bash
git clone https://github.com/ninazikovaa/projektno-nalogo.git
### 2.Open the project directtory
'''bash
    cd projectno-nalogo
Create a virtual environment
    pyhon -m venv .venv
Activate the virtual environment
    .venv\Scripts\Activate.ps1
Install the required libraries
    The project uses the following Python libraries:

    Pandas
    NumPy
    Matplotlib
    Seaborn
    Jupyter
    Notebook
    IPyKernel
Run the data cleaning process
    python src/data_cleaning.py
    This loads the raw Airbnb dataset, cleans the data, removes invalid and extreme values, creates additional variables, and saves the cleaned dataset.
Run the sttistical analysis
    python src/analysis.py
    This performs statistical analysis of prices, ratings, reviews, room types, neighbourhoods, Superhosts, correlations, and best-value listings.
Generate the visualizations
    python -c "import pandas as pd; from src.visualization import *; df=pd.read_csv('data/processed/skopje_airbnb_clean.csv'); prepare_output_directory(); plot_price_distribution(df); plot_price_by_room_type(df); plot_rating_distribution(df); plot_price_vs_rating(df); plot_reviews_vs_rating(df); plot_price_vs_capacity(df); plot_superhost_comparison(df); plot_neighbourhood_prices(df); plot_correlation_matrix(df)"
Open the Jupyter Notebook
    jupyter notebook
    then open notebooks/skopje_airbnb_analysis.ipynb


---
## Data Source

The dataset contains Airbnb listings from Skopje,
North Macedonia.

The data was obtained from:

https://doorstepanalytics.com/report?country=North_Macedonia&location=Skopje

The original dataset contains 2,398 listings and 68 columns.

After the cleaning process, the final dataset contains
2,148 listings and 70 columns.

---
Nina Zikova


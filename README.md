# Airbnb Skopje Data Analysis

## Project Description

This project analyzes Airbnb listings in Skopje, North Macedonia.

The main goal of the project is to collect, clean, process, analyze, and visualize Airbnb data in order to identify patterns in prices, ratings, reviews, accommodation types, and host characteristics.

The project uses Python and Jupyter Notebook for data analysis and visualization.

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

## How to Run the Project

### 1. Clone the repository

git clone https://github.com/ninazikovaa/projektno-nalogo.git

### 2. Open the project directory

cd projektno-nalogo

### 3. Create a virtual environment

python -m venv .venv

### 4. Activate the virtual environment

On Windows PowerShell:

.venv\Scripts\Activate.ps1

### 5. Install the required libraries

The project uses the following Python libraries:

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter
- Notebook
- IPyKernel

Install them with:

pip install pandas numpy matplotlib seaborn jupyter notebook ipykernel

### 6. Run the data cleaning process

python src/data_cleaning.py

This loads the raw Airbnb dataset, cleans the data, removes invalid and extreme values, creates additional variables, and saves the cleaned dataset.

### 7. Run the statistical analysis

python src/analysis.py

This performs statistical analysis of prices, ratings, reviews, room types, neighbourhoods, Superhosts, correlations, and best-value listings.

### 8. Generate the visualizations

python -c "import pandas as pd; from src.visualization import *; df=pd.read_csv('data/processed/skopje_airbnb_clean.csv'); prepare_output_directory(); plot_price_distribution(df); plot_price_by_room_type(df); plot_rating_distribution(df); plot_price_vs_rating(df); plot_reviews_vs_rating(df); plot_price_vs_capacity(df); plot_superhost_comparison(df); plot_neighbourhood_prices(df); plot_correlation_matrix(df)"

The generated graphs are saved in the results/figures/ directory.

### 9. Open the Jupyter Notebook

jupyter notebook

Then open:

notebooks/skopje_airbnb_analysis.ipynb

The notebook presents the main results of the analysis together with tables, explanations, and visualizations.

---

## Data Source

The dataset contains Airbnb listings from Skopje, North Macedonia.

The data was obtained from:

https://doorstepanalytics.com/report?country=North_Macedonia&location=Skopje

The original dataset contains 2,398 listings and 68 columns.

After the cleaning process, the final dataset contains 2,148 listings and 70 columns.

---

## Data Processing

The data cleaning process includes:

- cleaning column names
- removing duplicate rows
- converting numerical variables
- removing invalid prices
- detecting and removing extreme price values using the IQR method
- checking rating values
- creating additional variables

Two derived variables were created:

- price_per_guest
- price_per_bedroom

---

## Analysis

The project includes analysis of:

- Airbnb price distribution
- prices by room type
- rating distribution
- relationship between price and rating
- relationship between reviews and rating
- relationship between price and guest capacity
- Superhost versus non-Superhost performance
- neighbourhood price differences
- correlations between numerical variables
- best-value Airbnb listings

---

## Main Results

The cleaned dataset contains 2,148 Airbnb listings.

The average nightly price is approximately $56.27, while the median nightly price is approximately $52.85.

The average Airbnb rating is approximately 4.78 out of 5.

The analysis shows that Superhosts have a higher average rating and a substantially higher average number of reviews than non-Superhosts.

Guest capacity has a positive relationship with nightly price, while the relationship between price and rating is relatively weak.

---

## Technologies

The project is developed using:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Author

Nina Zikova
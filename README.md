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

## Data Source

The dataset contains Airbnb listings from Skopje,
North Macedonia.

The data was obtained from:

https://doorstepanalytics.com/report?country=North_Macedonia&location=Skopje

The original dataset contains 2,398 listings and 68 columns.

After the cleaning process, the final dataset contains
2,148 listings and 70 columns.

---

## Project Structure

```text
AirBnB-Skopje/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── skopje_airbnb_analysis.ipynb
│
├── results/
│   └── figures/
│
├── src/
│   ├── data_collection.py
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── visualization.py
│
├── .gitignore
├── README.md
└── requirements.txt
# Airbnb Skopje Data Analysis

## Project Description

This project analyzes Airbnb listings in Skopje, North Macedonia. The goal is to explore prices, ratings, reviews, room types, neighbourhoods, and host characteristics using Python and Jupyter Notebook.

## Research Questions

The analysis focuses on:

* What is the typical Airbnb price in Skopje?
* Which room types are the most expensive?
* Is there a connection between price and rating?
* Do Superhosts have better ratings?
* How are reviews related to ratings?
* Does guest capacity affect price?
* How do prices differ between neighbourhoods?
* Which listings offer the best value?

## Data

The dataset was obtained from Doorstep Analytics and originally contains 2,398 listings and 68 columns.

After cleaning, the dataset contains 2,148 listings and 70 columns.

## Data Processing

The data was cleaned by:

* removing duplicates and invalid values
* converting numerical columns
* removing extreme prices using the IQR method
* checking rating values
* creating `price_per_guest` and `price_per_bedroom`

## Analysis

The project includes statistical analysis and visualizations of prices, ratings, reviews, room types, guest capacity, Superhosts, neighbourhoods, and correlations between variables.

## Main Results

After cleaning, the average nightly price is about **$56.27**, with a median of **$52.85**. The average rating is around **4.78/5**.

Superhosts generally have higher ratings and more reviews than non-Superhosts. Guest capacity has a positive relationship with price, while the relationship between price and rating is relatively weak.





## Author

Nina Zikova

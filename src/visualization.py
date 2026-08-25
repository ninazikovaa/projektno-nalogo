"""
Visualization functions for Airbnb analysis in Skopje.
"""

from pathlib import Path  # Import Path for working with file paths

import matplotlib  # Import matplotlib for creating visualizations

# Use a non-interactive backend so that graphs can be saved as image files
matplotlib.use("Agg")

import matplotlib.pyplot as plt  # Import pyplot for creating and formatting plots
import seaborn as sns  # Import seaborn for statistical visualizations


# Define the directory where all generated figures will be saved
FIGURES_DIR = Path("results/figures")


def prepare_output_directory():
    """Create the directory for saved figures."""

    # Create the output directory if it does not already exist
    FIGURES_DIR.mkdir(
        parents=True,  # Create parent directories if necessary
        exist_ok=True,  # Do not raise an error if the directory already exists
    )


def plot_price_distribution(df):
    """Show the distribution of nightly prices."""

    # Create a new figure with a width of 10 and height of 6 inches
    plt.figure(figsize=(10, 6))

    # Create a histogram showing the distribution of nightly prices
    sns.histplot(
        data=df,  # Use the Airbnb DataFrame as the data source
        x="basicnightprice_usd",  # Use nightly price in USD for the x-axis
        bins=30,  # Divide the prices into 30 intervals
        kde=True,  # Add a smooth density curve to the histogram
    )

    # Add a descriptive title to the graph
    plt.title(
        "Distribution of Airbnb Prices in Skopje"
    )

    # Label the x-axis
    plt.xlabel("Price per night (USD)")

    # Label the y-axis
    plt.ylabel("Number of listings")

    # Automatically adjust the layout to prevent overlapping elements
    plt.tight_layout()

    # Save the graph as a high-resolution PNG image
    plt.savefig(
        FIGURES_DIR / "price_distribution.png",
        dpi=300,  # Use 300 dots per inch for good image quality
    )

    # Close the figure to free memory
    plt.close()


def plot_price_by_room_type(df):
    """Compare average prices by room type."""

    # Group the listings by room type and calculate the average price
    data = (
        df.groupby("roomtype_clean")
        ["basicnightprice_usd"]
        .mean()
        .sort_values(ascending=False)  # Sort room types by average price
    )

    # Create a new figure
    plt.figure(figsize=(10, 6))

    # Create a bar chart showing the average price for each room type
    data.plot(kind="bar")

    # Add a descriptive title
    plt.title(
        "Average Airbnb Price by Room Type"
    )

    # Label the x-axis
    plt.xlabel("Room type")

    # Label the y-axis
    plt.ylabel("Average price (USD)")

    # Rotate x-axis labels to make them easier to read
    plt.xticks(rotation=30)

    # Adjust the graph layout
    plt.tight_layout()

    # Save the graph as a PNG image
    plt.savefig(
        FIGURES_DIR / "price_by_room_type.png",
        dpi=300,
    )

    # Display the graph
    plt.show()


def plot_rating_distribution(df):
    """Show the distribution of Airbnb ratings."""

    # Create a new figure
    plt.figure(figsize=(10, 6))

    # Create a histogram showing the distribution of ratings
    sns.histplot(
        data=df,  # Use the Airbnb DataFrame
        x="starrating",  # Use the overall rating as the x-axis variable
        bins=20,  # Divide the ratings into 20 intervals
        kde=True,  # Add a smooth density curve
    )

    # Add a descriptive title
    plt.title(
        "Distribution of Airbnb Ratings in Skopje"
    )

    # Label the x-axis
    plt.xlabel("Rating")

    # Label the y-axis
    plt.ylabel("Number of listings")

    # Adjust the graph layout
    plt.tight_layout()

    # Save the graph as a PNG image
    plt.savefig(
        FIGURES_DIR / "rating_distribution.png",
        dpi=300,
    )

    # Display the graph
    plt.show()


def plot_price_vs_rating(df):
    """Show the relationship between price and rating."""

    # Remove rows where either price or rating is missing
    data = df.dropna(
        subset=[
            "basicnightprice_usd",  # Required price variable
            "starrating",  # Required rating variable
        ]
    )

    # Create a new figure
    plt.figure(figsize=(10, 6))

    # Create a scatter plot comparing price and rating
    sns.scatterplot(
        data=data,  # Use the filtered dataset
        x="basicnightprice_usd",  # Use price as the x-axis variable
        y="starrating",  # Use rating as the y-axis variable
        alpha=0.5,  # Make points partially transparent
    )

    # Add a descriptive title
    plt.title(
        "Price vs. Rating"
    )

    # Label the x-axis
    plt.xlabel("Price per night (USD)")

    # Label the y-axis
    plt.ylabel("Rating")

    # Adjust the graph layout
    plt.tight_layout()

    # Save the graph as a PNG image
    plt.savefig(
        FIGURES_DIR / "price_vs_rating.png",
        dpi=300,
    )

    # Display the graph
    plt.show()


def plot_reviews_vs_rating(df):
    """Show the relationship between reviews and rating."""

    # Remove rows where review count or rating is missing
    data = df.dropna(
        subset=[
            "reviewcount",  # Required review count variable
            "starrating",  # Required rating variable
        ]
    )

    # Create a new figure
    plt.figure(figsize=(10, 6))

    # Create a scatter plot comparing reviews and ratings
    sns.scatterplot(
        data=data,  # Use the filtered dataset
        x="reviewcount",  # Use number of reviews as the x-axis variable
        y="starrating",  # Use rating as the y-axis variable
        alpha=0.5,  # Make points partially transparent
    )

    # Add a descriptive title
    plt.title(
        "Number of Reviews vs. Rating"
    )

    # Label the x-axis
    plt.xlabel("Number of reviews")

    # Label the y-axis
    plt.ylabel("Rating")

    # Adjust the graph layout
    plt.tight_layout()

    # Save the graph as a PNG image
    plt.savefig(
        FIGURES_DIR / "reviews_vs_rating.png",
        dpi=300,
    )

    # Display the graph
    plt.show()


def plot_price_vs_capacity(df):
    """Show the relationship between price and capacity."""

    # Create a new figure
    plt.figure(figsize=(10, 6))

    # Create a scatter plot comparing price and guest capacity
    sns.scatterplot(
        data=df,  # Use the Airbnb DataFrame
        x="personcapacity",  # Use guest capacity as the x-axis variable
        y="basicnightprice_usd",  # Use nightly price as the y-axis variable
        alpha=0.5,  # Make points partially transparent
    )

    # Add a descriptive title
    plt.title(
        "Price vs. Guest Capacity"
    )

    # Label the x-axis
    plt.xlabel("Number of guests")

    # Label the y-axis
    plt.ylabel("Price per night (USD)")

    # Adjust the graph layout
    plt.tight_layout()

    # Save the graph as a PNG image
    plt.savefig(
        FIGURES_DIR / "price_vs_capacity.png",
        dpi=300,
    )

    # Display the graph
    plt.show()


def plot_superhost_comparison(df):
    """Compare Superhosts and non-Superhosts."""

    # Group listings by Superhost status and calculate the average rating
    data = (
        df.groupby("host_issuperhost")
        ["starrating"]
        .mean()
    )

    # Define readable labels for the two host categories
    labels = [
        "Non-Superhost",
        "Superhost",
    ]

    # Get the average rating for each host category
    values = [
        data.get(False, 0),  # Average rating of non-Superhosts
        data.get(True, 0),  # Average rating of Superhosts
    ]

    # Create a new figure
    plt.figure(figsize=(8, 6))

    # Create a bar chart comparing the two host categories
    plt.bar(
        labels,
        values,
    )

    # Add a descriptive title
    plt.title(
        "Average Rating: Superhosts vs. Non-Superhosts"
    )

    # Label the x-axis
    plt.xlabel("Host type")

    # Label the y-axis
    plt.ylabel("Average rating")

    # Limit the y-axis to the possible rating range
    plt.ylim(0, 5)

    # Adjust the graph layout
    plt.tight_layout()

    # Save the graph as a PNG image
    plt.savefig(
        FIGURES_DIR / "superhost_rating.png",
        dpi=300,
    )

    # Display the graph
    plt.show()


def plot_neighbourhood_prices(df):
    """Show average price for the most common neighbourhoods."""

    # Remove listings without neighbourhood information
    # and group the remaining listings by neighbourhood
    data = (
        df.dropna(subset=["neighbourhood"])
        .groupby("neighbourhood")
        .agg(
            # Count the number of listings in each neighbourhood
            listings=(
                "basicnightprice_usd",
                "count",
            ),

            # Calculate the average price in each neighbourhood
            average_price=(
                "basicnightprice_usd",
                "mean",
            ),
        )
    )

    # Keep only neighbourhoods with at least 10 listings
    # to avoid misleading results from very small samples
    data = (
        data[data["listings"] >= 10]

        # Sort neighbourhoods by average price from highest to lowest
        .sort_values(
            "average_price",
            ascending=False,
        )

        # Keep only the 15 most expensive qualifying neighbourhoods
        .head(15)
    )

    # Create a new figure with a larger size for neighbourhood names
    plt.figure(figsize=(12, 7))

    # Create a bar chart of average neighbourhood prices
    data["average_price"].plot(
        kind="bar",
    )

    # Add a descriptive title
    plt.title(
        "Average Airbnb Price by Neighbourhood"
    )

    # Label the x-axis
    plt.xlabel("Neighbourhood")

    # Label the y-axis
    plt.ylabel("Average price (USD)")

    # Rotate neighbourhood names for better readability
    plt.xticks(rotation=45)

    # Adjust the graph layout
    plt.tight_layout()

    # Save the graph as a PNG image
    plt.savefig(
        FIGURES_DIR / "neighbourhood_prices.png",
        dpi=300,
    )

    # Display the graph
    plt.show()


def plot_correlation_matrix(df):
    """Show the correlation matrix."""

    # Define the numerical variables that should be included
    # in the correlation analysis
    columns = [
        "basicnightprice_usd",  # Nightly price
        "price_per_guest",  # Price per guest
        "price_per_bedroom",  # Price per bedroom
        "personcapacity",  # Maximum number of guests
        "bedrooms",  # Number of bedrooms
        "beds",  # Number of beds
        "reviewcount",  # Number of reviews
        "starrating",  # Overall rating
        "locationrating",  # Location rating
        "cleanlinessrating",  # Cleanliness rating
        "valuerating",  # Value rating
        "accuracyrating",  # Accuracy rating
        "checkinrating",  # Check-in rating
        "communicationrating",  # Communication rating
    ]

    # Keep only variables that actually exist in the DataFrame
    available = [
        column
        for column in columns
        if column in df.columns
    ]

    # Calculate the correlation matrix
    correlation = df[available].corr()

    # Create a large figure so that all variables are readable
    plt.figure(figsize=(13, 10))

    # Display the correlation matrix as a heatmap
    sns.heatmap(
        correlation,  # Use the calculated correlation matrix
        annot=True,  # Display the correlation values inside the cells
        fmt=".2f",  # Format correlation values to two decimal places
        cmap="coolwarm",  # Use a diverging colour map for positive and negative correlations
        center=0,  # Place zero in the centre of the colour scale
    )

    # Add a descriptive title
    plt.title(
        "Correlation Matrix of Airbnb Variables"
    )

    # Adjust the graph layout
    plt.tight_layout()

    # Save the correlation matrix as a high-resolution PNG image
    plt.savefig(
        FIGURES_DIR / "correlation_matrix.png",
        dpi=300,
    )

    # Display the correlation matrix
    plt.show()
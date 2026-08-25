"""
Statistical analysis of Airbnb listings in Skopje.
"""

from pathlib import Path  # Import Path for working with file paths

import pandas as pd  # Import pandas for data analysis and manipulation


# Define the path to the cleaned Airbnb dataset
CLEAN_FILE = Path(
    "data/processed/skopje_airbnb_clean.csv"
)


def load_data(file_path: Path) -> pd.DataFrame:
    """Load the cleaned Airbnb dataset."""

    # Read the CSV file and store it as a pandas DataFrame
    return pd.read_csv(file_path)


def dataset_overview(
    df: pd.DataFrame,
) -> dict:
    """Return basic information about the dataset."""

    # Return the main descriptive values of the dataset
    return {
        # Count the total number of listings
        "listings": len(df),

        # Count the total number of columns
        "columns": len(df.columns),

        # Calculate the average nightly price
        "average_price": df[
            "basicnightprice_usd"
        ].mean(),

        # Calculate the median nightly price
        "median_price": df[
            "basicnightprice_usd"
        ].median(),

        # Calculate the average Airbnb rating
        "average_rating": df[
            "starrating"
        ].mean(),

        # Calculate the average number of reviews
        "average_reviews": df[
            "reviewcount"
        ].mean(),
    }


def price_statistics(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Calculate descriptive statistics for prices."""

    # Select the price-related columns and calculate descriptive statistics
    return df[
        [
            "basicnightprice_usd",  # Nightly price in USD
            "price_per_guest",  # Price per guest
            "price_per_bedroom",  # Price per bedroom
        ]
    ].describe()  # Calculate count, mean, standard deviation, minimum, quartiles and maximum


def rating_statistics(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Calculate descriptive statistics for ratings."""

    # Select all available rating variables
    return df[
        [
            "starrating",  # Overall Airbnb rating
            "locationrating",  # Rating for the location
            "cleanlinessrating",  # Rating for cleanliness
            "valuerating",  # Rating for value for money
            "accuracyrating",  # Rating for listing accuracy
            "checkinrating",  # Rating for the check-in process
            "communicationrating",  # Rating for host communication
        ]
    ].describe()  # Calculate descriptive statistics for all rating columns


def review_statistics(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Calculate descriptive statistics for reviews."""

    # Select the columns containing information about reviews
    return df[
        [
            "reviewcount",  # Total number of reviews
            "visible_review_count",  # Number of visible reviews
        ]
    ].describe()  # Calculate descriptive statistics for the review variables


def price_by_room_type(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Calculate price statistics by room type."""

    # Group the listings according to their room type
    return (
        df.groupby("roomtype_clean")
        .agg(
            # Count the number of listings in each room type
            listings=(
                "basicnightprice_usd",
                "count",
            ),

            # Calculate the average price for each room type
            average_price=(
                "basicnightprice_usd",
                "mean",
            ),

            # Calculate the median price for each room type
            median_price=(
                "basicnightprice_usd",
                "median",
            ),

            # Calculate the average rating for each room type
            average_rating=(
                "starrating",
                "mean",
            ),
        )

        # Sort room types from the highest to the lowest average price
        .sort_values(
            "average_price",
            ascending=False,
        )
    )


def price_by_neighbourhood(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Calculate price statistics by neighbourhood."""

    # Remove listings where neighbourhood information is missing
    return (
        df.dropna(subset=["neighbourhood"])

        # Group the remaining listings by neighbourhood
        .groupby("neighbourhood")

        # Calculate several statistics for each neighbourhood
        .agg(
            # Count the number of listings
            listings=(
                "basicnightprice_usd",
                "count",
            ),

            # Calculate the average nightly price
            average_price=(
                "basicnightprice_usd",
                "mean",
            ),

            # Calculate the median nightly price
            median_price=(
                "basicnightprice_usd",
                "median",
            ),

            # Calculate the average rating
            average_rating=(
                "starrating",
                "mean",
            ),
        )

        # Sort neighbourhoods from the most expensive to the least expensive
        .sort_values(
            "average_price",
            ascending=False,
        )
    )


def host_analysis(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Compare Superhosts with other hosts."""

    # Group listings according to whether the host is a Superhost
    return (
        df.groupby("host_issuperhost")

        # Calculate statistics for each host group
        .agg(
            # Count the number of listings for each host group
            listings=(
                "airbnb_listingid",
                "count",
            ),

            # Calculate the average nightly price
            average_price=(
                "basicnightprice_usd",
                "mean",
            ),

            # Calculate the average rating
            average_rating=(
                "starrating",
                "mean",
            ),

            # Calculate the average number of reviews
            average_reviews=(
                "reviewcount",
                "mean",
            ),
        )
    )


def correlation_analysis(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Calculate correlations between numerical variables."""

    # Define the numerical variables that are useful for correlation analysis
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

    # Keep only the columns that actually exist in the dataset
    available_columns = [
        column
        for column in columns
        if column in df.columns
    ]

    # Calculate the correlation matrix for the available numerical columns
    return df[available_columns].corr()


def best_value_listings(
    df: pd.DataFrame,
    minimum_rating: float = 4.5,
    minimum_reviews: int = 5,
    number: int = 20,
) -> pd.DataFrame:
    """
    Find highly rated listings with relatively low prices.
    """

    # Keep only listings that satisfy the minimum rating and review requirements
    filtered = df[
        (df["starrating"] >= minimum_rating)
        & (df["reviewcount"] >= minimum_reviews)
    ].copy()

    # Calculate a custom value score using rating divided by price
    filtered["value_score"] = (
        filtered["starrating"]
        / filtered["basicnightprice_usd"]
    )

    # Define the columns that should be included in the final result
    columns = [
        "listingtitle",  # Name of the Airbnb listing
        "basicnightprice_usd",  # Nightly price
        "starrating",  # Overall rating
        "reviewcount",  # Number of reviews
        "roomtype_clean",  # Type of accommodation
        "value_score",  # Calculated value score
    ]

    # Sort listings by value score and return only the requested number
    return (
        filtered
        .sort_values(
            "value_score",
            ascending=False,  # Put the highest value scores first
        )
        [columns]
        .head(number)  # Return only the top listings
    )


def main() -> None:
    """Run the complete statistical analysis."""

    # Load the cleaned dataset
    df = load_data(CLEAN_FILE)

    # Print the main title of the analysis
    print("\nAIRBNB SKOPJE ANALYSIS")

    # Print a separator line
    print("=" * 40)

    # Calculate the general overview of the dataset
    overview = dataset_overview(df)

    # Print the total number of Airbnb listings
    print(
        f"Number of listings: "
        f"{overview['listings']:,}"
    )

    # Print the total number of columns
    print(
        f"Number of columns: "
        f"{overview['columns']}"
    )

    # Print the average nightly price rounded to two decimal places
    print(
        f"Average price: "
        f"${overview['average_price']:.2f}"
    )

    # Print the median nightly price rounded to two decimal places
    print(
        f"Median price: "
        f"${overview['median_price']:.2f}"
    )

    # Print the average Airbnb rating
    print(
        f"Average rating: "
        f"{overview['average_rating']:.2f}"
    )

    # Print the average number of reviews
    print(
        f"Average number of reviews: "
        f"{overview['average_reviews']:.2f}"
    )

    # Print the title for the price statistics section
    print("\nPRICE STATISTICS")

    # Print a separator line
    print("=" * 40)

    # Calculate and print descriptive price statistics
    print(price_statistics(df))

    # Print the title for the rating statistics section
    print("\nRATING STATISTICS")

    # Print a separator line
    print("=" * 40)

    # Calculate and print descriptive rating statistics
    print(rating_statistics(df))

    # Print the title for the room type analysis
    print("\nPRICE BY ROOM TYPE")

    # Print a separator line
    print("=" * 40)

    # Calculate and print price statistics grouped by room type
    print(price_by_room_type(df))

    # Print the title for the neighbourhood analysis
    print("\nTOP NEIGHBOURHOODS BY PRICE")

    # Print a separator line
    print("=" * 40)

    # Calculate neighbourhood statistics and display the top 10
    print(
        price_by_neighbourhood(df).head(10)
    )

    # Print the title for the Superhost analysis
    print("\nSUPERHOST ANALYSIS")

    # Print a separator line
    print("=" * 40)

    # Calculate and print statistics comparing Superhosts and non-Superhosts
    print(host_analysis(df))

    # Print the title for the correlation analysis
    print("\nCORRELATION ANALYSIS")

    # Print a separator line
    print("=" * 40)

    # Calculate and print the correlation matrix
    print(correlation_analysis(df))

    # Print the title for the best-value listings
    print("\nBEST VALUE LISTINGS")

    # Print a separator line
    print("=" * 40)

    # Calculate and print the top 20 best-value listings
    print(best_value_listings(df))


# Run the main function only when this file is executed directly
if __name__ == "__main__":
    main()
"""
Clean and prepare Airbnb data for analysis.
"""

from pathlib import Path  # Import Path for handling file paths

import pandas as pd  # Import pandas for working with tabular data


# Define the location of the original raw dataset
RAW_FILE = Path(
    "data/raw/skopje_airbnb_raw.csv"
)

# Define the location where the cleaned dataset will be saved
PROCESSED_FILE = Path(
    "data/processed/skopje_airbnb_clean.csv"
)


def load_data(file_path: Path) -> pd.DataFrame:
    """Load the raw Airbnb dataset."""

    # Read the CSV file and return it as a pandas DataFrame
    return pd.read_csv(file_path)


def clean_column_names(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Convert column names to a consistent format."""

    # Create a copy so that the original DataFrame is not modified
    df = df.copy()

    # Clean all column names and convert them to a consistent format
    df.columns = (
        df.columns
        .str.strip()  # Remove unnecessary spaces at the beginning and end
        .str.lower()  # Convert all characters to lowercase
        .str.replace(" ", "_")  # Replace spaces with underscores
    )

    # Return the DataFrame with cleaned column names
    return df


def remove_duplicates(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Remove duplicate rows."""

    # Remove rows that are exact duplicates of other rows
    return df.drop_duplicates()


def convert_numeric_columns(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Convert relevant columns to numeric values."""

    # Define columns that should contain numerical values
    numeric_columns = [
        "bathrooms",  # Number of bathrooms
        "bedrooms",  # Number of bedrooms
        "beds",  # Number of beds
        "personcapacity",  # Maximum number of guests
        "picturecount",  # Number of pictures
        "reviewcount",  # Number of reviews
        "starrating",  # Overall rating
        "locationrating",  # Location rating
        "cleanlinessrating",  # Cleanliness rating
        "valuerating",  # Value rating
        "accuracyrating",  # Accuracy rating
        "checkinrating",  # Check-in rating
        "communicationrating",  # Communication rating
        "basicnightprice",  # Basic nightly price
        "basicnightprice_usd",  # Basic nightly price in USD
        "taxes",  # Taxes in the original currency
        "taxes_usd",  # Taxes in USD
        "outlierprice_perbedroom",  # Price per bedroom from the source
        "outlierprice_perguest",  # Price per guest from the source
        "lat",  # Latitude coordinate
        "lng",  # Longitude coordinate
    ]

    # Create a copy of the DataFrame before modifying it
    df = df.copy()

    # Go through every column that should contain numerical data
    for column in numeric_columns:

        # Check whether the column exists in the dataset
        if column in df.columns:

            # Convert the column to numeric values
            # Invalid values are converted to missing values
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce",
            )

    # Return the DataFrame with converted numeric columns
    return df


def clean_prices(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Remove invalid and extreme price values."""

    # Create a copy so that the original DataFrame is preserved
    df = df.copy()

    # Define the column containing the nightly price in USD
    price_column = "basicnightprice_usd"

    # Stop the function if the required price column does not exist
    if price_column not in df.columns:
        return df

    # Remove listings where the price is missing
    df = df[
        df[price_column].notna()
    ]

    # Remove listings with zero or negative prices
    df = df[
        df[price_column] > 0
    ]

    # Calculate the first quartile of the price distribution
    q1 = df[price_column].quantile(0.25)

    # Calculate the third quartile of the price distribution
    q3 = df[price_column].quantile(0.75)

    # Calculate the interquartile range
    iqr = q3 - q1

    # Calculate the lower limit for detecting price outliers
    lower_bound = q1 - 1.5 * iqr

    # Calculate the upper limit for detecting price outliers
    upper_bound = q3 + 1.5 * iqr

    # Display the calculated lower price boundary
    print(
        f"Price IQR lower bound: "
        f"${lower_bound:.2f}"
    )

    # Display the calculated upper price boundary
    print(
        f"Price IQR upper bound: "
        f"${upper_bound:.2f}"
    )

    # Store the number of rows before removing outliers
    before = len(df)

    # Keep only prices inside the calculated IQR boundaries
    df = df[
        (df[price_column] >= lower_bound)
        & (df[price_column] <= upper_bound)
    ]

    # Calculate how many extreme price values were removed
    removed = before - len(df)

    # Display the number of removed price outliers
    print(
        f"Extreme price values removed: "
        f"{removed}"
    )

    # Return the cleaned DataFrame
    return df


def clean_ratings(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Remove impossible rating values."""

    # Create a copy of the DataFrame
    df = df.copy()

    # Check whether the overall rating column exists
    if "starrating" in df.columns:

        # Replace ratings outside the valid 0-5 range with missing values
        df.loc[
            (df["starrating"] < 0)
            | (df["starrating"] > 5),
            "starrating",
        ] = pd.NA

    # Return the DataFrame with cleaned ratings
    return df


def create_derived_variables(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Create additional variables for analysis."""

    # Create a copy of the DataFrame
    df = df.copy()

    # Check whether price and guest capacity are available
    if {
        "basicnightprice_usd",
        "personcapacity",
    }.issubset(df.columns):

        # Calculate the nightly price per guest
        df["price_per_guest"] = (
            df["basicnightprice_usd"]
            / df["personcapacity"]
        )

    # Check whether price and bedroom information are available
    if {
        "basicnightprice_usd",
        "bedrooms",
    }.issubset(df.columns):

        # Calculate the nightly price per bedroom
        df["price_per_bedroom"] = (
            df["basicnightprice_usd"]
            / df["bedrooms"]
        )

    # Return the DataFrame with the new variables
    return df


def clean_dataset(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Run the complete cleaning pipeline."""

    # Display a message showing that the cleaning process has started
    print("Starting data cleaning...")

    # Store the original number of rows for comparison later
    original_rows = len(df)

    # Standardize the column names
    df = clean_column_names(df)

    # Confirm that column names were cleaned
    print("Column names cleaned.")

    # Remove duplicate rows
    df = remove_duplicates(df)

    # Calculate and display the number of removed duplicates
    print(
        f"Duplicates removed: "
        f"{original_rows - len(df)}"
    )

    # Convert appropriate columns to numeric data types
    df = convert_numeric_columns(df)

    # Confirm that numeric conversion is complete
    print("Numeric columns converted.")

    # Remove invalid and extreme price values
    df = clean_prices(df)

    # Confirm that price cleaning is complete
    print("Invalid prices removed.")

    # Check and clean invalid rating values
    df = clean_ratings(df)

    # Confirm that rating validation is complete
    print("Ratings checked.")

    # Create additional variables for further analysis
    df = create_derived_variables(df)

    # Confirm that derived variables were created
    print("Derived variables created.")

    # Return the completely cleaned DataFrame
    return df


def save_clean_data(
    df: pd.DataFrame,
    file_path: Path,
) -> None:
    """Save cleaned data to CSV."""

    # Create the output directory if it does not already exist
    file_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Save the cleaned DataFrame as a CSV file
    df.to_csv(
        file_path,
        index=False,  # Do not save the DataFrame index as a column
    )

    # Display the location of the saved cleaned dataset
    print(
        f"Clean dataset saved to: {file_path}"
    )


def main() -> None:
    """Execute the complete cleaning process."""

    # Display a message showing that the raw dataset is being loaded
    print("Loading raw dataset...")

    # Load the original raw Airbnb dataset
    df = load_data(RAW_FILE)

    # Display the original dimensions of the dataset
    print(
        f"Original dataset: "
        f"{len(df):,} rows, "
        f"{len(df.columns)} columns"
    )

    # Run the complete data cleaning pipeline
    cleaned_df = clean_dataset(df)

    # Display the dimensions of the cleaned dataset
    print(
        f"Cleaned dataset: "
        f"{len(cleaned_df):,} rows, "
        f"{len(cleaned_df.columns)} columns"
    )

    # Save the cleaned dataset to the processed data directory
    save_clean_data(
        cleaned_df,
        PROCESSED_FILE,
    )


# Run the main function only when this script is executed directly
if __name__ == "__main__":
    main()
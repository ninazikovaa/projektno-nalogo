"""
Collect Airbnb data for Skopje.

The dataset is obtained from an online source and
stored locally as a raw CSV file.
"""

from pathlib import Path  # Import Path for working with file paths

import pandas as pd  # Import pandas for reading and working with CSV data


# Define the location of the raw Airbnb dataset
RAW_FILE = Path(
    "data/raw/skopje_airbnb_raw.csv"
)

# Store the URL of the online data source
SOURCE_URL = (
    "https://doorstepanalytics.com/"
    "report?country=North_Macedonia&location=Skopje"
)


def load_raw_data(file_path: Path) -> pd.DataFrame:
    """Load the downloaded Airbnb dataset."""

    # Read the raw CSV file and return it as a pandas DataFrame
    return pd.read_csv(file_path)


def show_dataset_information(
    df: pd.DataFrame,
) -> None:
    """Display basic information about the dataset."""

    # Print the title of the dataset information section
    print("Airbnb Skopje dataset")

    # Print a separator line
    print("-" * 40)

    # Display the total number of Airbnb listings
    print(f"Number of listings: {len(df):,}")

    # Display the total number of columns in the dataset
    print(f"Number of columns: {len(df.columns)}")

    # Display the URL from which the dataset was obtained
    print(f"Data source: {SOURCE_URL}")


def main() -> None:
    """Load and inspect the raw dataset."""

    # Check whether the raw dataset file exists
    if not RAW_FILE.exists():

        # Stop the program and provide an informative error message
        raise FileNotFoundError(
            f"Dataset not found: {RAW_FILE}"
        )

    # Load the raw Airbnb dataset
    df = load_raw_data(RAW_FILE)

    # Display basic information about the loaded dataset
    show_dataset_information(df)


# Run the main function only when this script is executed directly
if __name__ == "__main__":
    main()
import pandas as pd

def load_metadata(path: str, nrows: int = None) -> pd.DataFrame:
    """Load metadata.csv into a pandas DataFrame."""
    return pd.read_csv(path, nrows=nrows)

def clean_metadata(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and prepare the metadata DataFrame."""
    # Convert publish_time to datetime
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    # Extract year
    df["year"] = df["publish_time"].dt.year
    # Handle abstracts: replace missing with empty string
    df["abstract"] = df["abstract"].fillna("")
    # Add word count for abstracts
    df["abstract_word_count"] = df["abstract"].apply(lambda x: len(str(x).split()))
    return df

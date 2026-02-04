import pandas as pd
import os
import glob
from .logger import get_logger

logger = get_logger("INGESTION")

def ingest_data(file_pattern):
    """
    Reads data from files matching the pattern.
    Supports CSV and JSON.
    """
    logger.info(f"Starting data ingestion for pattern: {file_pattern}")
    
    files = glob.glob(file_pattern)
    if not files:
        logger.warning(f"No files found for pattern: {file_pattern}")
        return pd.DataFrame()

    dfs = []
    for file in files:
        try:
            if file.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.endswith('.json'):
                df = pd.read_json(file)
            else:
                logger.warning(f"Unsupported file format: {file}")
                continue
            dfs.append(df)
            logger.info(f"Successfully loaded {file} with shape {df.shape}")
        except Exception as e:
            logger.error(f"Failed to load {file}: {e}")

    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
        logger.info(f"Ingestion completed. Total shape: {combined_df.shape}")
        return combined_df
    else:
        logger.warning("No data loaded.")
        return pd.DataFrame()

if __name__ == "__main__":
    # Example usage
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    df = ingest_data(os.path.join(data_dir, "*.csv"))
    print(df.head())

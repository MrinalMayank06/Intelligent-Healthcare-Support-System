from pathlib import Path
import pandas as pd


def load_raw_data(path: str = "data/raw/patient_encounters.csv") -> pd.DataFrame:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Raw data not found: {file_path}")
    return pd.read_csv(file_path)

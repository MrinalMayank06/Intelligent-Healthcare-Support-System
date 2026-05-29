import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    for col in cleaned.columns:
        if cleaned[col].dtype == 'object':
            cleaned[col] = cleaned[col].fillna('unknown')
        else:
            cleaned[col] = cleaned[col].fillna(cleaned[col].median())
    return cleaned.drop_duplicates()

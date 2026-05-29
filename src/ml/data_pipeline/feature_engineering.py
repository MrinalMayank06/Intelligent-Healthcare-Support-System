import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    # Domain-specific feature placeholder: keeps demo simple and explainable.
    data['risk_age_band'] = data['age'].apply(lambda x: 'child' if x < 12 else 'senior' if x > 65 else 'adult')
    return data

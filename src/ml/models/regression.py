from sklearn.ensemble import RandomForestRegressor


def build_regressor() -> RandomForestRegressor:
    return RandomForestRegressor(n_estimators=80, random_state=42)

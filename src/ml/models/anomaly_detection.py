from sklearn.ensemble import IsolationForest


def build_anomaly_model() -> IsolationForest:
    return IsolationForest(contamination=0.08, random_state=42)

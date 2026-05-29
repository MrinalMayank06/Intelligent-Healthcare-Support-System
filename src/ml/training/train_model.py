from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from joblib import dump
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import IsolationForest, RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.ml.data_pipeline.loader import load_raw_data
from src.ml.data_pipeline.preprocessing import clean_data
from src.ml.data_pipeline.feature_engineering import create_features

FEATURES = ['age', 'primary_symptom', 'fever', 'oxygen_saturation', 'heart_rate', 'pain_level', 'symptom_days', 'chronic_condition']
CATEGORICAL = ['primary_symptom']
TARGET = "triage_level"
PROBLEM_TYPE = "classification"
MODEL_PATH = Path("artifacts/models/triage_model.joblib")
METRICS_PATH = Path("artifacts/metrics/training_metrics.json")


def train() -> dict:
    raw = load_raw_data()
    data = create_features(clean_data(raw))
    Path("data/curated").mkdir(parents=True, exist_ok=True)
    data.to_csv("data/curated/healthcare_triage_dataset.csv", index=False)

    X = data[FEATURES]
    y = data[TARGET]
    numeric = [c for c in FEATURES if c not in CATEGORICAL]
    preprocessor = ColumnTransformer([
        ("num", StandardScaler(), numeric),
        ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL),
    ])
    estimator = RandomForestRegressor(n_estimators=80, random_state=42) if PROBLEM_TYPE == "regression" else RandomForestClassifier(n_estimators=120, random_state=42, class_weight="balanced")
    model = Pipeline([("preprocess", preprocessor), ("model", estimator)])
    stratify = y if PROBLEM_TYPE != "regression" else None
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=stratify)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    metrics = {"rows": int(len(data)), "target": TARGET, "features": FEATURES, "model": "RandomForestClassifier for symptom triage"}
    if PROBLEM_TYPE == "regression":
        metrics.update({"mae": float(mean_absolute_error(y_test, predictions)), "r2": float(r2_score(y_test, predictions))})
    else:
        metrics.update({"accuracy": float(accuracy_score(y_test, predictions)), "class_distribution": {str(k): int(v) for k, v in y.value_counts().to_dict().items()}})

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    METRICS_PATH.parent.mkdir(parents=True, exist_ok=True)
    dump(model, MODEL_PATH)
    METRICS_PATH.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    numeric_df = data[numeric]
    anomaly = IsolationForest(contamination=0.08, random_state=42).fit(numeric_df)
    dump(anomaly, "artifacts/models/anomaly_model.joblib")
    return metrics


if __name__ == "__main__":
    print(train())

from __future__ import annotations

import pandas as pd
from pathlib import Path


class AnalyticsAgent:
    def __init__(self, dataset_path: str = "data/curated/healthcare_triage_dataset.csv"):
        self.dataset_path = dataset_path

    def summarize(self, question: str = "") -> dict:
        path = Path(self.dataset_path)
        if not path.exists():
            return {"summary": "Curated dataset not found. Run scripts/run_training.py first.", "question": question}
        df = pd.read_csv(path)
        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        summary = {col: float(df[col].mean()) for col in numeric_cols[:8]}
        return {
            "question": question,
            "rows": int(len(df)),
            "numeric_column_means": summary,
            "business_note": "Use these values as dashboard KPIs and compare model output against domain thresholds."
        }

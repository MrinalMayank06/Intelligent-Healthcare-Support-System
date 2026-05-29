from __future__ import annotations

from pathlib import Path
import pandas as pd
from joblib import load

MODEL_PATH = Path("artifacts/models/triage_model.joblib")


def predict(payload: dict) -> dict:
    if not MODEL_PATH.exists():
        return {"prediction": None, "message": "Model file missing. Run python scripts/run_training.py first."}
    model = load(MODEL_PATH)
    df = pd.DataFrame([payload])
    pred = model.predict(df)[0]
    proba = None
    if hasattr(model, "predict_proba"):
        try:
            classes = list(model.classes_)
            probs = model.predict_proba(df)[0]
            proba = {str(cls): float(prob) for cls, prob in zip(classes, probs)}
        except Exception:
            proba = None
    return {
        "prediction": str(pred) if not isinstance(pred, (int, float)) else float(pred),
        "probability": proba,
        "model_path": str(MODEL_PATH),
        "business_meaning": "Predicted triage level: Emergency, Urgent or Routine. This is decision-support and must be validated by a clinician."
    }

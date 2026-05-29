from __future__ import annotations

from src.ml.inference.predict import predict
from src.database.collections import PREDICTION_COLLECTION
from src.database.crud import insert_one


class PredictionService:
    """Application service that keeps route code thin and reusable."""

    def run_prediction(self, payload: dict) -> dict:
        result = predict(payload)
        insert_one(PREDICTION_COLLECTION, {"input": payload, "output": result})
        return result

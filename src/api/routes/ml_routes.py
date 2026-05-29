from fastapi import APIRouter
from src.api.schemas.request_models import PredictionRequest
from src.api.utils.response_formatter import ok
from src.ml.inference.predict import predict
from src.database.crud import insert_one
from src.database.collections import PREDICTION_COLLECTION

router = APIRouter(prefix="/api/v1/ml", tags=["ML Prediction"])


@router.post("/predict")
def predict_route(payload: PredictionRequest):
    result = predict(payload.model_dump())
    insert_one(PREDICTION_COLLECTION, {"input": payload.model_dump(), "output": result})
    return ok(result, "Prediction generated")

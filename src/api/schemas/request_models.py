from pydantic import BaseModel, Field
from typing import Any, Dict


class IngestRequest(BaseModel):
    record: Dict[str, Any] = Field(..., description="Raw Healthcare record")


class PredictionRequest(BaseModel):
    age: float
    primary_symptom: str
    fever: float
    oxygen_saturation: float
    heart_rate: float
    pain_level: float
    symptom_days: float
    chronic_condition: float

    model_config = {
        "json_schema_extra": {
            "example": {
            "age": 67,
        "primary_symptom": "breathing_issue",
        "fever": 1,
        "oxygen_saturation": 91,
        "heart_rate": 112,
        "pain_level": 8,
        "symptom_days": 3,
        "chronic_condition": 1
            }
        }
    }


class AgentRequest(BaseModel):
    question: str = Field(..., min_length=3, description="User question for multi-agent system")
    user_role: str = "analyst"


class DocumentSearchRequest(BaseModel):
    query: str = Field(..., min_length=3)
    top_k: int = 3

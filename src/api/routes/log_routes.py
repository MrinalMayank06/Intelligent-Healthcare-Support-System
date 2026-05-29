from fastapi import APIRouter
from src.api.utils.response_formatter import ok
from src.database.crud import find_recent
from src.database.collections import AGENT_LOG_COLLECTION, PREDICTION_COLLECTION

router = APIRouter(prefix="/api/v1/logs", tags=["Logs"])


@router.get("/agents")
def agent_logs(limit: int = 5):
    return ok(find_recent(AGENT_LOG_COLLECTION, limit), "Recent agent logs")


@router.get("/predictions")
def prediction_logs(limit: int = 5):
    return ok(find_recent(PREDICTION_COLLECTION, limit), "Recent prediction logs")

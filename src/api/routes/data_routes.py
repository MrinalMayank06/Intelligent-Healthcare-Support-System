from fastapi import APIRouter
from src.api.schemas.request_models import IngestRequest
from src.api.utils.response_formatter import ok
from src.database.collections import DATA_COLLECTION
from src.database.crud import insert_one, find_recent

router = APIRouter(prefix="/api/v1/data", tags=["Data Ingestion"])


@router.post("/ingest")
def ingest(payload: IngestRequest):
    result = insert_one(DATA_COLLECTION, payload.record)
    return ok({"storage": result, "record": payload.record}, "Record ingested")


@router.get("/recent")
def recent(limit: int = 5):
    return ok(find_recent(DATA_COLLECTION, limit), "Recent records")

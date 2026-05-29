from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List

from src.database.mongo_client import get_database
from src.common.logger import get_logger

logger = get_logger(__name__)
_MEMORY_STORE: dict[str, list[dict[str, Any]]] = {}


def _with_timestamp(document: Dict[str, Any]) -> Dict[str, Any]:
    copy = dict(document)
    copy.setdefault("created_at", datetime.now(timezone.utc).isoformat())
    return copy


def insert_one(collection_name: str, document: Dict[str, Any]) -> Dict[str, Any]:
    document = _with_timestamp(document)
    db = get_database()
    if db is None:
        _MEMORY_STORE.setdefault(collection_name, []).append(document)
        return {"inserted_id": f"memory-{len(_MEMORY_STORE[collection_name])}", "stored_in": "memory"}
    result = db[collection_name].insert_one(document)
    return {"inserted_id": str(result.inserted_id), "stored_in": "mongodb"}


def find_recent(collection_name: str, limit: int = 10) -> List[Dict[str, Any]]:
    db = get_database()
    if db is None:
        return list(reversed(_MEMORY_STORE.get(collection_name, [])))[0:limit]
    docs = db[collection_name].find().sort("created_at", -1).limit(limit)
    return [{**doc, "_id": str(doc.get("_id"))} for doc in docs]

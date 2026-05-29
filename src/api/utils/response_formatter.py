from datetime import datetime, timezone
from typing import Any


def ok(data: Any, message: str = "success") -> dict:
    return {
        "status": "success",
        "message": message,
        "data": data,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def fail(message: str, details: Any = None) -> dict:
    return {
        "status": "failed",
        "message": message,
        "details": details,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

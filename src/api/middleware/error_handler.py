from fastapi import Request
from fastapi.responses import JSONResponse
from src.common.exceptions import AppError
from src.api.utils.response_formatter import fail
from src.common.logger import get_logger

logger = get_logger(__name__)


async def app_error_handler(request: Request, exc: AppError):
    logger.error("Application error on %s: %s", request.url.path, exc.message)
    return JSONResponse(status_code=exc.status_code, content=fail(exc.message))


async def unhandled_error_handler(request: Request, exc: Exception):
    logger.exception("Unhandled error on %s", request.url.path)
    return JSONResponse(status_code=500, content=fail("Internal server error", str(exc)))

from fastapi import FastAPI
from src.api.routes import data_routes, ml_routes, agent_routes, analytics_routes, mcp_routes, log_routes
from src.api.middleware.error_handler import app_error_handler, unhandled_error_handler
from src.common.exceptions import AppError

app = FastAPI(
    title="Intelligent Healthcare Support System",
    description="Symptom triage, medical information assistant and patient analytics platform.",
    version="1.0.0",
)

app.add_exception_handler(AppError, app_error_handler)
app.add_exception_handler(Exception, unhandled_error_handler)

app.include_router(data_routes.router)
app.include_router(ml_routes.router)
app.include_router(agent_routes.router)
app.include_router(analytics_routes.router)
app.include_router(mcp_routes.router)
app.include_router(log_routes.router)


@app.get("/health")
def health():
    return {"status": "healthy", "project": "Intelligent Healthcare Support System"}


@app.get("/api/v1/status")
def status():
    return {
        "status": "running",
        "domain": "Healthcare",
        "mandatory_components": ["FastAPI", "ML", "RAG", "Multi-Agent", "Azure-ready", "Power BI-ready"],
    }

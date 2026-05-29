from fastapi import APIRouter
from src.api.utils.response_formatter import ok
from src.agents.analytics_agent.agent import AnalyticsAgent

router = APIRouter(prefix="/api/v1/analytics", tags=["Analytics"])
analytics = AnalyticsAgent()


@router.get("/kpis")
def kpis():
    return ok(analytics.summarize("Give KPI summary"), "KPI summary generated")

from __future__ import annotations

from src.agents.analytics_agent.agent import AnalyticsAgent


class AnalyticsService:
    """Service used by routes and dashboard exports."""

    def __init__(self):
        self.agent = AnalyticsAgent()

    def kpis(self) -> dict:
        return self.agent.summarize("Generate dashboard KPI summary")

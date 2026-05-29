from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List

from src.agents.mcp.tool_registry import ToolRegistry
from src.agents.support_agent.rag_pipeline import RAGPipeline
from src.agents.analytics_agent.agent import AnalyticsAgent


class MCPOrchestrator:
    # Lightweight MCP-style orchestrator.
    # It follows MCP thinking: user intent -> tool selection -> trace -> response.

    def __init__(self):
        self.registry = ToolRegistry()
        self.rag = RAGPipeline()
        self.analytics = AnalyticsAgent()
        self.trace: List[Dict[str, Any]] = []
        self.registry.register("rag_search", self.rag.answer)
        self.registry.register("analytics_summary", self.analytics.summarize)

    def route(self, question: str) -> dict:
        started_at = datetime.now(timezone.utc).isoformat()
        lower = question.lower()
        tool_name = "analytics_summary" if any(word in lower for word in ["kpi", "trend", "analytics", "metric", "dashboard"]) else "rag_search"
        result = self.registry.call(tool_name, question=question)
        step = {"time": started_at, "selected_tool": tool_name, "question": question, "result_preview": str(result)[:250]}
        self.trace.append(step)
        return {"selected_tool": tool_name, "result": result, "trace": self.trace[-5:]}

    def get_trace(self) -> list[dict]:
        return self.trace[-20:]

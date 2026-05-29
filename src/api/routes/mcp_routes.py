from fastapi import APIRouter
from src.api.utils.response_formatter import ok
from src.agents.mcp.mcp_orchestrator import MCPOrchestrator

router = APIRouter(prefix="/api/v1/mcp", tags=["MCP Trace"])
orchestrator = MCPOrchestrator()


@router.get("/trace")
def trace():
    return ok(orchestrator.get_trace(), "Latest orchestration trace")

from fastapi import APIRouter
from src.api.schemas.request_models import AgentRequest, DocumentSearchRequest, PredictionRequest
from src.api.utils.response_formatter import ok
from src.agents.mcp.mcp_orchestrator import MCPOrchestrator
from src.agents.support_agent.rag_pipeline import RAGPipeline
from src.agents.triage_agent.agent import TriageAgent
from src.database.crud import insert_one
from src.database.collections import AGENT_LOG_COLLECTION

router = APIRouter(prefix="/api/v1", tags=["GenAI Agents"])
orchestrator = MCPOrchestrator()
rag = RAGPipeline()
domain_agent = TriageAgent()


@router.post("/agents/ask")
def ask_agent(payload: AgentRequest):
    result = orchestrator.route(payload.question)
    insert_one(AGENT_LOG_COLLECTION, {"question": payload.question, "result": result})
    return ok(result, "Agent response generated")


@router.post("/agents/domain-advice")
def domain_advice(payload: PredictionRequest, question: str = "Explain result and next action"):
    result = domain_agent.advise(payload.model_dump(), question)
    return ok(result, "Domain agent advice generated")


@router.post("/documents/search")
def search_documents(payload: DocumentSearchRequest):
    result = rag.answer(payload.query)
    return ok(result, "Document search completed")

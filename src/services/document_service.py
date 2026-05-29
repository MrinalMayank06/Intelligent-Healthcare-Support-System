from __future__ import annotations

from src.agents.support_agent.rag_pipeline import RAGPipeline


class DocumentService:
    """Wrapper over the RAG pipeline for document/knowledge search APIs."""

    def __init__(self):
        self.rag = RAGPipeline()

    def search(self, query: str) -> dict:
        return self.rag.answer(query)

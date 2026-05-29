from __future__ import annotations

from src.agents.support_agent.vector_store import search_knowledge
from src.agents.shared.llm_client import LLMClient


class RAGPipeline:
    def __init__(self, embeddings_path: str = "artifacts/knowledge/knowledge_embeddings.json"):
        self.embeddings_path = embeddings_path
        self.llm = LLMClient()

    def answer(self, question: str) -> dict:
        matches = search_knowledge(question, self.embeddings_path, top_k=3)
        context = "\n".join([f"- {m['title']}: {m['content']}" for m in matches])
        prompt = "Answer using retrieved knowledge. Mention uncertainty when context is weak."
        answer = self.llm.generate(prompt, question, context)
        return {"answer": answer, "retrieved_context": matches}

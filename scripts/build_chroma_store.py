from src.agents.support_agent.vector_store import build_embeddings

if __name__ == "__main__":
    rows = build_embeddings("artifacts/knowledge/knowledge_base.csv", "artifacts/knowledge/knowledge_embeddings.json")
    print(f"Built {len(rows)} lightweight knowledge embeddings.")

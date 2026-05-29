from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict

import pandas as pd


def simple_embed(text: str) -> set[str]:
    return {token.strip(".,:;!?()[]{}'").lower() for token in text.split() if len(token) > 2}


def build_embeddings(knowledge_csv: str, output_json: str) -> list[dict]:
    df = pd.read_csv(knowledge_csv)
    rows = []
    for _, row in df.iterrows():
        text = f"{row.get('title', '')} {row.get('content', '')}"
        rows.append({"title": row.get("title", ""), "content": row.get("content", ""), "tokens": sorted(simple_embed(text))})
    Path(output_json).parent.mkdir(parents=True, exist_ok=True)
    Path(output_json).write_text(json.dumps(rows, indent=2), encoding="utf-8")
    return rows


def search_knowledge(query: str, embeddings_json: str, top_k: int = 3) -> List[Dict]:
    path = Path(embeddings_json)
    if not path.exists():
        return []
    query_tokens = simple_embed(query)
    rows = json.loads(path.read_text(encoding="utf-8"))
    scored = []
    for row in rows:
        tokens = set(row.get("tokens", []))
        score = len(query_tokens & tokens)
        scored.append({**row, "score": score})
    return sorted(scored, key=lambda item: item["score"], reverse=True)[:top_k]

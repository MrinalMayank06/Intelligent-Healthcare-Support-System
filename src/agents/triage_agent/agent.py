from __future__ import annotations

from src.agents.shared.llm_client import LLMClient
from src.ml.inference.predict import predict


class TriageAgent:
    def __init__(self):
        self.llm = LLMClient()

    def advise(self, payload: dict, question: str = "") -> dict:
        prediction = predict(payload)
        system_prompt = "You are a healthcare support assistant. Explain model output safely, avoid diagnosis, and recommend clinician/emergency escalation for red-flag symptoms."
        context = f"Model output: {prediction}\nInput payload: {payload}"
        answer = self.llm.generate(system_prompt, question or "Explain the model output and next action", context)
        return {"prediction": prediction, "agent_answer": answer}

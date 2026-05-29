from __future__ import annotations

from src.common.settings import get_settings
from src.common.logger import get_logger

logger = get_logger(__name__)


class LLMClient:
    # Small Azure OpenAI wrapper with safe local fallback.
    # In local technical walkthrough/demo, fallback mode returns a deterministic answer so the
    # project runs even without paid keys. On Azure, set USE_AZURE_OPENAI=true.

    def __init__(self):
        self.settings = get_settings()

    def generate(self, system_prompt: str, user_prompt: str, context: str = "") -> str:
        if not self.settings.use_azure_openai:
            return self._fallback(system_prompt, user_prompt, context)
        try:
            from openai import AzureOpenAI

            client = AzureOpenAI(
                azure_endpoint=self.settings.azure_openai_endpoint,
                api_key=self.settings.azure_openai_api_key,
                api_version=self.settings.azure_openai_api_version,
            )
            response = client.chat.completions.create(
                model=self.settings.azure_openai_deployment,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{user_prompt}"},
                ],
                temperature=0.2,
            )
            return response.choices[0].message.content or "No response generated."
        except Exception as exc:
            logger.warning("Azure OpenAI call failed, using fallback. Error: %s", exc)
            return self._fallback(system_prompt, user_prompt, context)

    @staticmethod
    def _fallback(system_prompt: str, user_prompt: str, context: str = "") -> str:
        trimmed_context = context[:700] if context else "No retrieved context available."
        return (
            "Fallback agent response: I reviewed the available platform context and "
            f"question. Context summary: {trimmed_context}. "
            f"Recommended next action for '{user_prompt}': check the dashboard metrics, "
            "verify model prediction, and escalate if business risk is high."
        )

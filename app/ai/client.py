from google import genai

from app.ai.config import GEMINI_API_KEY, GEMINI_MODEL
from app.ai.provider import AIProvider


class AIClient:
    """Send prompts to the selected AI provider."""

    def __init__(self, provider: AIProvider) -> None:
        self.provider = provider

        if self.provider == AIProvider.GEMINI:
            self.client = genai.Client(api_key=GEMINI_API_KEY)
        else:
            raise ValueError(
                f"Unsupported AI provider: {self.provider.value}"
            )

    def ask(self, prompt: str) -> str:
        """Send a prompt to the AI provider and return the response text."""

        if not prompt.strip():
            raise ValueError("The prompt cannot be empty.")

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )

        if not response.text:
            raise RuntimeError("Gemini returned an empty response.")

        return response.text
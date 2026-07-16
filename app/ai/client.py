from app.ai.provider import AIProvider


class AIClient:

    def __init__(self, provider: AIProvider):
        self.provider = provider

    def ask(self, prompt: str):

        print("=" * 40)
        print("AI Provider:", self.provider.value)
        print("=" * 40)

        print(prompt)

        return "Fake AI Response"
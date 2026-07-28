from pathlib import Path
from app.services.document_reader import read_word_document
from app.ai.client import AIClient
from app.ai.provider import AIProvider
from app.services.prompt_loader import load_prompt


def main() -> None:
    """Run the first version of Advisor AI Studio."""

    document_path = Path("data/documents/sample.docx")

    print("=" * 50)
    print("Advisor AI Studio - Document Reader")
    print("=" * 50)

    try:
        document_text = read_word_document(document_path)

        print("\nDocument extracted successfully:\n")
        print(document_text)

        client = AIClient(AIProvider.GEMINI)

        prompt = load_prompt("meeting_summary.txt")
        prompt = prompt.replace("{{DOCUMENT}}",document_text)

        response = client.ask(prompt)

        print("\nAI Response:\n")
        print(response)

    except (FileNotFoundError, ValueError) as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()


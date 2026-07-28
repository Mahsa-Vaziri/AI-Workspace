from pathlib import Path
from app.ai.client import AIClient
from app.ai.provider import AIProvider
from app.services.document_reader import read_word_document
from app.services.output_writer import save_markdown
from app.services.prompt_loader import load_prompt
from app.services.word_writer import save_word_document


def main() -> None:
    """Run Advisor AI Studio."""

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
        prompt = prompt.replace(
            "{{DOCUMENT}}",
            document_text,
        )

        print("\nSending document to Gemini...")

        response = client.ask(prompt)

        print("\nAI Response:\n")
        print(response)

        output_file = save_markdown(
            "meeting_summary.md",
            response,
        )
        print(f"\nReport saved to: {output_file}")

        word_file = save_word_document(
        "meeting_summary.docx",
        response,
        )

        print(f"Word report saved to: {word_file}")


    except Exception as error:
        print(f"\nError: {type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
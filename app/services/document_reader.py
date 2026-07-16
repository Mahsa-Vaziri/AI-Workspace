from pathlib import Path

from docx import Document


def read_word_document(file_path: str | Path) -> str:
    """
    Read a Microsoft Word document and return its non-empty paragraphs
    as one text string.

    Args:
        file_path: Path to a .docx file.

    Returns:
        Extracted document text.

    Raises:
        FileNotFoundError: If the document does not exist.
        ValueError: If the selected file is not a .docx document.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {path}")

    if path.suffix.lower() != ".docx":
        raise ValueError("Only .docx files are currently supported.")

    document = Document(path)

    paragraphs = [
        paragraph.text.strip()
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ]

    return "\n".join(paragraphs)
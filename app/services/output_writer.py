from pathlib import Path


def save_markdown(file_name: str, content: str) -> Path:
    """
    Save AI output as a Markdown file.
    """

    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)

    file_path = output_folder / file_name

    file_path.write_text(content, encoding="utf-8")

    return file_path
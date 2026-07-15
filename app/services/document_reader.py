from docx import Document


def read_word_document(file_path):
    """
    Reads a Word document and returns its text.
    """

    doc = Document(file_path)

    text = []

    for paragraph in doc.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)
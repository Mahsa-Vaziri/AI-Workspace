from services.document_reader import read_word_document

print("Advisor AI Studio")

text = read_word_document("data/documents/sample.docx")

print(text)
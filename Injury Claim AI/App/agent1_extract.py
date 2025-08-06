# agent1_extract.py
from docx import Document
import io

async def extract_text_from_docx(upload_file):
    contents = await upload_file.read()
    doc = Document(io.BytesIO(contents))
    data = {}

    for para in doc.paragraphs:
        line = para.text.strip()
        if ':' in line:
            key, value = line.split(':', 1)
            data[key.strip().lower()] = value.strip()

    return data

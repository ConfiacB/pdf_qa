import fitz  # PyMuPDF

def extract_text_from_pdf(path: str) -> str:
    """Read the PDF and extract the text"""
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)

def chunk_text(text, max_length=500, overlap=50):
    """Split the text into small parts (called "chunks")"""
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_length - overlap):
        chunk = " ".join(words[i:i + max_length])
        chunks.append(chunk)
    return chunks

# index_ppc.py

from App.vector_store import index_pdf_to_vector_store

if __name__ == "__main__":
    pdf_path = "documents/Constitution.pdf"
    index_pdf_to_vector_store(pdf_path)
    print("✅ PPC document indexed into Chroma vector store!")

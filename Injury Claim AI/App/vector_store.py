# import os
# from langchain_community.vectorstores import Chroma
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_core.documents import Document
# from langchain_text_splitters import CharacterTextSplitter

# CHROMA_PATH = "chroma_db"

# # Initialize embedding model
# embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# def get_vector_store():
#     return Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding)

# def index_case_to_vector_store(case_obj):
#     text = f"""
#     Name: {case_obj.name}
#     Crime: {case_obj.crime}
#     Location: {case_obj.location}
#     Punishment: {case_obj.punishment}
#     Date: {case_obj.date}
#     Report: {case_obj.full_report}
#     """

#     splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
#     docs = splitter.create_documents([text])
#     vectordb = get_vector_store()
#     vectordb.add_documents(docs)












# # vector_store.py
# import os
# from langchain_community.vectorstores import Chroma
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_community.document_loaders import PyMuPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter
# from langchain_core.documents import Document
# from dotenv import load_dotenv
# load_dotenv()


# CHROMA_PATH = "chroma_db"
# embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# # Load vector store
# def get_vector_store():
#     return Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding)

# # Index structured case object
# def index_case_to_vector_store(case_obj):
#     text = f"""
#     Name: {case_obj.name}
#     Crime: {case_obj.crime}
#     Location: {case_obj.location}
#     Punishment: {case_obj.punishment}
#     Date: {case_obj.date}
#     Report: {case_obj.full_report}
#     """
#     splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
#     docs = splitter.create_documents([text])
#     vectordb = get_vector_store()
#     vectordb.add_documents(docs)

# # Index legal PDF documents like PPC or Instructions to Courts
# def index_pdf_to_vector_store(pdf_path):
#     loader = PyMuPDFLoader(pdf_path)
#     docs = loader.load()

#     splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
#     texts = splitter.split_documents(docs)

#     vectordb = get_vector_store()
#     vectordb.add_documents(texts)
#     vectordb.persist()







# App/vector_store.py

import os
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()

# Path for Chroma vector DB
CHROMA_PATH = "chroma_db"

# Google embeddings model for semantic vectorization
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Load or initialize vector store
def get_vector_store():
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding)

# Index structured injury claim object to vector DB
def index_injury_claim_to_vector_store(claim_obj):
    text = f"""
    Full Name: {claim_obj.full_name}
    Date of Birth: {claim_obj.dob}
    Phone: {claim_obj.phone}
    Email: {claim_obj.email}
    Incident Location: {claim_obj.incident_location}
    Incident Date: {claim_obj.incident_date}
    Injury Description: {claim_obj.injury_description}
    Recommended Action: {claim_obj.recommended_action}
    Relevant Laws: {claim_obj.relevant_laws}
    Full Report: {claim_obj.full_report}
    """
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.create_documents([text])

    vectordb = get_vector_store()
    vectordb.add_documents(docs)

# Index legal reference PDFs (Labor laws, safety policies, etc.)
def index_pdf_to_vector_store(pdf_path):
    loader = PyMuPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = splitter.split_documents(docs)

    vectordb = get_vector_store()
    vectordb.add_documents(texts)
    vectordb.persist()








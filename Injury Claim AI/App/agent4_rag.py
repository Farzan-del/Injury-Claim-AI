# # App/agent4_rag.py
# from App.llm_config import get_gemini_llm
# from App.vector_store import get_vector_store
# from langchain.chains import RetrievalQA

# def answer_question_with_rag(query: str) -> str:
#     retriever = get_vector_store().as_retriever()
#     qa_chain = RetrievalQA.from_chain_type(
#         llm=get_gemini_llm(),
#         retriever=retriever,
#         return_source_documents=False
#     )
#     result = qa_chain.run(query)
#     return result









# App/agent4_rag.py
from App.llm_config import get_gemini_llm
from App.vector_store import get_vector_store
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def answer_injury_claim_question(query: str) -> str:
    retriever = get_vector_store().as_retriever()

    # Optional: Inject legal context into the prompt
    legal_context = (
        "You are a legal assistant specializing in workplace injury compensation under Pakistani labor law. "
        "Use the following documents and knowledge base to answer user questions clearly and helpfully.\n\n"
        f"Question: {query}"
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=get_gemini_llm(),
        retriever=retriever,
        return_source_documents=False
    )

    result = qa_chain.run(legal_context)
    return result

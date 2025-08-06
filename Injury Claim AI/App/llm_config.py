# llm_config.py
from langchain_google_genai import ChatGoogleGenerativeAI

def get_gemini_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.3
    )

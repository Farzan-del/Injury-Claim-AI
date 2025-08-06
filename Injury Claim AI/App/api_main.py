# # api_main.py
# from fastapi import FastAPI, UploadFile, File
# from App.agent1_extract import extract_text_from_docx
# from App.agent2_report import generate_criminal_report
# from App.agent3_lawresearch import research_similar_cases
# from App.db import store_case
# from App.agent4_rag import answer_question_with_rag
# app = FastAPI()

# @app.post("/analyze-form/")
# async def analyze_form(file: UploadFile = File(...)):
#     # Step 1: Extract info
#     form_text = await extract_text_from_docx(file)
 
#     # Step 2: Generate report
#     report = generate_criminal_report(form_text)

#     # Step 3: Research past cases and suggest punishment
#     legal_insight = research_similar_cases(report)

#     # Step 4: Compile final analysis
#     final_analysis = {
#         "extracted_data": form_text,
#         "generated_report": report,
#         "legal_research": legal_insight
#     }

#     # Step 5: Store case
#     store_case(final_analysis)

#     return final_analysis
# @app.post("/ask_rag")
# def ask_rag(query: str):
#     answer = answer_question_with_rag(query)
#     return {"answer": answer}








# from fastapi import FastAPI, UploadFile, File
# from App.agent1_extract import extract_text_from_docx
# from App.agent2_report import generate_criminal_report
# from App.agent3_lawresearch import research_similar_cases
# from App.db import store_case
# from App.agent4_rag import answer_question_with_rag
# import json
# from datetime import datetime

# app = FastAPI()

# @app.post("/analyze-form/")
# async def analyze_form(file: UploadFile = File(...)):
#     form_text = await extract_text_from_docx(file)
#     report = generate_criminal_report(form_text)
#     legal_insight = research_similar_cases(report)

#     final_analysis = {
#         "extracted_data": form_text,
#         "generated_report": report,
#         "legal_research": legal_insight,
#         "ppc_section": legal_insight.get("ppc_section", "N/A")
#     }

#     store_case(final_analysis)

#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     with open(f"Cases/case_{timestamp}.json", "w") as f:
#         json.dump(final_analysis, f, indent=4)

#     return final_analysis

# @app.post("/ask_rag")
# def ask_rag(query: str):
#     answer = answer_question_with_rag(query)
#     return {"answer": answer}

# # ✅ New index_ppc.py
# from App.vector_store import index_pdf_to_vector_store









# from fastapi import FastAPI, UploadFile, File
# from App.agent1_extract import extract_text_from_docx
# from App.agent2_report import generate_criminal_report
# from App.agent3_lawresearch import search_similar_cases  # updated function
# from App.db import store_case
# from App.agent4_rag import answer_question_with_rag

# app = FastAPI()

# @app.post("/analyze-form/")
# async def analyze_form(file: UploadFile = File(...)):
#     # Step 1: Extract info
#     form_text = await extract_text_from_docx(file)

#     # Step 2: Generate report
#     report = generate_criminal_report(form_text)

#     # Step 3: Research past cases using Tavily
#     legal_insight = await search_similar_cases(report)

#     # Step 4: Compile final analysis
#     final_analysis = {
#         "extracted_data": form_text,
#         "generated_report": report,
#         "legal_research": legal_insight,
#         "ppc_section": legal_insight.get("ppc_section", "N/A")
#     }

#     # Step 5: Store case in DB
#     store_case(final_analysis)

#     return final_analysis

# @app.post("/ask_rag")
# def ask_rag(query: str):
#     answer = answer_question_with_rag(query)
#     return {"answer": answer}





















# api_main.py

from fastapi import FastAPI, UploadFile, File
from App.agent1_extract import extract_text_from_docx
from App.agent2_report import generate_injury_claim_report
from App.agent3_lawresearch import research_similar_injury_cases
from App.db import store_injury_claim
from App.agent4_rag import answer_injury_claim_question

app = FastAPI()

from fastapi import UploadFile, File

@app.post("/analyze-form/")
async def analyze_form(file: UploadFile = File(...)):
    # Step 1: Extract form data
    form_text = await extract_text_from_docx(file)

    # Step 2: Generate formal report
    report = generate_injury_claim_report(form_text)

    # ✅ Step 3: Extract crime and location from form_text
    crime = form_text.get("crime", "")
    location = form_text.get("location", "")

    # ✅ Step 4: Run legal research using Gemini
    legal_insight = research_similar_injury_cases(crime, location)

    # ✅ Step 5: Final structure
    final_analysis = {
        "extracted_data": form_text,
        "generated_report": report,
        "legal_research": legal_insight,
        "ppc_section": legal_insight[0].get("ppc_section", "N/A") if legal_insight else "N/A"
    }

    return final_analysis


@app.post("/ask_rag")
def ask_rag(query: str):
    answer = answer_injury_claim_question(query)
    return {"answer": answer}

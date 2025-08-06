# def research_similar_cases(report):
#     # This can be replaced by actual LLM or legal DB query
#     dummy_cases = [
#         {
#             "case": "Case A",
#             "crime": "Theft",
#             "punishment": "2 years imprisonment"
#         },
#         {
#             "case": "Case B",
#             "crime": "Theft",
#             "punishment": "3 years imprisonment"
#         }
#     ]

#     if "theft" in report.lower():
#         matched = [case for case in dummy_cases if case["crime"].lower() == "theft"]
#     else:
#         matched = [{"case": "No similar case found", "punishment": "To be decided by judge"}]

#     return {
#         "similar_cases": matched,
#         "recommended_punishment": matched[0]["punishment"] if matched else "Not Available"
#     }




















# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# import os
# from dotenv import load_dotenv

# # Load API key
# load_dotenv()

# # Setup Gemini model
# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=0.4,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )

# # Define the prompt to research past crimes
# prompt = ChatPromptTemplate.from_template("""
# You're a legal research assistant. Based on the following crime report:

# "{report}"

# Do the following:
# 1. Identify 1-2 real or typical past legal cases with the same crime.
# 2. Mention what punishment was assigned in those cases.
# 3. Recommend a suitable punishment for this new case.

# Reply in structured JSON format:
# {
#   "similar_cases": [
#     {"case": "...", "crime": "...", "punishment": "..."},
#     ...
#   ],
#   "recommended_punishment": "..."
# }
# """)

# def research_similar_cases(report):
#     # Build chain with Gemini
#     chain = prompt | llm
#     result = chain.invoke({"report": report})

#     import json
#     try:
#         return json.loads(result.content)  # Parse response safely
#     except Exception:
#         # Fallback structure if JSON parsing fails
#         return {
#             "similar_cases": [
#                 {"case": "No data", "crime": "N/A", "punishment": "Undetermined"}
#             ],
#             "recommended_punishment": "Undetermined"
#         }



















# # agent3_lawresearch.py
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.prompts.chat import HumanMessagePromptTemplate
# import os
# from dotenv import load_dotenv
# import json

# # Load API key from .env
# load_dotenv()

# # Create Gemini model instance
# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=0.4,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )

# # Define chat-style prompt template correctly
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You're a legal research assistant."),
#     ("human", """Based on the following crime report:

# \"\"\"{report}\"\"\"

# Do the following:
# 1. Identify 1-2 real or typical past legal cases with the same crime.
# 2. Mention what punishment was assigned in those cases.
# 3. Recommend a suitable punishment for this new case.

# Reply in structured JSON format:
# {{
#   "similar_cases": [
#     {{"case": "...", "crime": "...", "punishment": "..."}},
#     ...
#   ],
#   "recommended_punishment": "..."
# }}""")
# ])

# # Define the function to invoke the model
# def research_similar_cases(report):
#     chain = prompt | llm
#     result = chain.invoke({"report": report})

#     try:
#         return json.loads(result.content)
#     except Exception:
#         return {
#             "similar_cases": [
#                 {"case": "No data", "crime": "N/A", "punishment": "Undetermined"}
#             ],
#             "recommended_punishment": "Undetermined"
#         }


# # ✅ Updated agent3_lawresearch.py
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# import os
# from dotenv import load_dotenv
# import json

# load_dotenv()

# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=0.4,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a legal assistant specialized in Pakistan Penal Code."),
#     ("human", """Based on the following crime report:
# \"\"\"{report}\"\"\"

# 1. Identify 1-2 real or typical past legal cases in **Pakistan** with the same crime.
# 2. Mention punishment under **relevant sections of PPC**.
# 3. Recommend a suitable punishment under Pakistani law.

# Reply in structured JSON format:
# {
#   "similar_cases": [
#     {"case": "...", "crime": "...", "punishment": "...", "ppc_section": "..."}
#   ],
#   "recommended_punishment": "...",
#   "ppc_section": "..."
# }""")
# ])

# def research_similar_cases(report):
#     chain = prompt | llm
#     result = chain.invoke({"report": report})

#     try:
#         return json.loads(result.content)
#     except Exception:
#         return {
#             "similar_cases": [
#                 {"case": "No data", "crime": "N/A", "punishment": "Undetermined", "ppc_section": "N/A"}
#             ],
#             "recommended_punishment": "Undetermined",
#             "ppc_section": "N/A"
#         }











# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# import os
# from dotenv import  load_dotenv
# import json

# # Load API key
# load_dotenv()

# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=0.4,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )

# # Escape braces in JSON
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a legal assistant specialized in Pakistan Penal Code."),
#     ("human", """Based on the following crime report:

# \"\"\"{report}\"\"\"

# 1. Identify 1-2 real or typical past legal cases in **Pakistan** with the same crime.
# 2. Mention punishment under **relevant sections of PPC**.
# 3. Recommend a suitable punishment under Pakistani law.

# Reply in structured JSON format:
# {{
#   "similar_cases": [
#     {{"case": "...", "crime": "...", "punishment": "...", "ppc_section": "..."}}
#   ],
#   "recommended_punishment": "...",
#   "ppc_section": "..."
# }}
# """)
# ])

# def research_similar_cases(report):
#     chain = prompt | llm
#     result = chain.invoke({"report": report})

#     try:
#         return json.loads(result.content)
#     except Exception:
#         return {
#             "similar_cases": [
#                 {"case": "No data", "crime": "N/A", "punishment": "Undetermined", "ppc_section": "N/A"}
#             ],
#             "recommended_punishment": "Undetermined",
#             "ppc_section": "N/A"
#         }















# import os
# import json
# from dotenv import load_dotenv
# from tavily import TavilyClient

# # Load environment variables
# load_dotenv()

# # Initialize Tavily client
# client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# # Prompt format for the web search query
# def build_search_query(report_text: str) -> str:
#     return f"Similar legal cases in Pakistan for this report: {report_text}"

# # Function to extract structured info from search results
# def extract_case_info(results):
#     similar_cases = []
#     for result in results.get("results", [])[:2]:  # Limit to 2 results
#         content = result.get("content", "")
#         title = result.get("title", "Unnamed Case")
#         url = result.get("url", "")

#         # Attempt basic structure extraction
#         similar_cases.append({
#             "case": title,
#             "crime": "Theft or similar",  # You can improve this with NLP if needed
#             "punishment": "See source",
#             "ppc_section": "Section 379 (likely)",
#             "source": url
#         })

#     return similar_cases

# # Main function to call in your API
# def research_similar_cases(report: str):
#     try:
#         # Step 1: Search
#         response = client.search(
#             query=build_search_query(report),
#             search_depth="advanced",
#             include_answer=True
#         )

#         # Step 2: Extract structured data
#         similar_cases = extract_case_info(response)

#         return {
#             "similar_cases": similar_cases,
#             "recommended_punishment": "Refer to case sources for guidance",
#             "ppc_section": "Section 379" if "theft" in report.lower() else "Undetermined"
#         }

#     except Exception as e:
#         print("Tavily Error:", str(e))
#         return {
#             "similar_cases": [
#                 {"case": "No data", "crime": "N/A", "punishment": "Undetermined", "ppc_section": "N/A"}
#             ],
#             "recommended_punishment": "Undetermined",
#             "ppc_section": "N/A"
#         }






# # agent3_lawresearch.py

# from decouple import config
# from tavily import TavilyClient

# tavily_api_key = config("TAVILY_API_KEY")
# client = TavilyClient(api_key=tavily_api_key)

# def perform_legal_search(query):
#     if len(query) > 400:
#         return [{
#             "case": "Query too long",
#             "crime": "N/A",
#             "punishment": "Undetermined",
#             "ppc_section": "N/A"
#         }]
    
#     try:
#         response = client.search(query, search_depth="advanced", include_answer=True)
#         results = response.get("results", [])

#         # Parse and structure top 3 relevant results
#         structured_results = []
#         for result in results[:3]:
#             structured_results.append({
#                 "case": result.get("title") or "Unknown Case",
#                 "crime": query,  # just echo back for now
#                 "punishment": "To be inferred from source",
#                 "link": result.get("url")
#             })

#         return structured_results if structured_results else [{
#             "case": "No similar cases found",
#             "crime": query,
#             "punishment": "Unknown",
#             "ppc_section": "Unknown"
#         }]

#     except Exception as e:
#         return [{
#             "case": "Search error",
#             "crime": query,
#             "punishment": "API failed",
#             "ppc_section": "N/A",
#             "error": str(e)
#         }]
















# from decouple import config
# from tavily import TavilyClient

# tavily_api_key = config("TAVILY_API_KEY")
# client = TavilyClient(api_key=tavily_api_key)

# def research_similar_cases(crime: str, location: str):
#     query = f"Cases of {crime} in {location} under Pakistan Penal Code"

#     if len(query) > 400:
#         return [{
#             "case": "Query too long",
#             "crime": "N/A",
#             "punishment": "Undetermined",
#             "ppc_section": "N/A"
#         }]
    
#     try:
#         response = client.search(query, search_depth="advanced", include_answer=True)
#         results = response.get("results", [])

#         # Parse and structure top 3 relevant results
#         structured_results = []
#         for result in results[:3]:
#             structured_results.append({
#                 "case": result.get("title") or "Unknown Case",
#                 "crime": query,
#                 "punishment": "To be inferred from source",
#                 "link": result.get("url")
#             })

#         return structured_results if structured_results else [{
#             "case": "No similar cases found",
#             "crime": query,
#             "punishment": "Unknown",
#             "ppc_section": "Unknown"
#         }]

#     except Exception as e:
#         return [{
#             "case": "Search error",
#             "crime": query,
#             "punishment": "API failed",
#             "ppc_section": "N/A",
#             "error": str(e)
#         }]








from decouple import config
from tavily import TavilyClient

tavily_api_key = config("TAVILY_API_KEY")
client = TavilyClient(api_key=tavily_api_key)

def research_similar_injury_cases(injury_description: str, incident_location: str):
    """
    Searches for similar personal injury or workplace accident cases in Pakistan.
    """
    query = f"Similar workplace injury claims in {incident_location}, Pakistan. Case examples or legal actions related to: {injury_description}"

    if len(query) > 400:
        return [{
            "case": "Query too long",
            "incident": "N/A",
            "legal_action": "Undetermined",
            "labor_law_section": "N/A"
        }]

    try:
        response = client.search(query, search_depth="advanced", include_answer=True)
        results = response.get("results", [])

        # Structure top 3 relevant results
        structured_results = []
        for result in results[:3]:
            structured_results.append({
                "case": result.get("title") or "Unknown Case",
                "incident": injury_description,
                "legal_action": "To be inferred from source",
                "link": result.get("url")
            })

        return structured_results if structured_results else [{
            "case": "No similar cases found",
            "incident": injury_description,
            "legal_action": "Unknown",
            "labor_law_section": "Unknown"
        }]

    except Exception as e:
        return [{
            "case": "Search error",
            "incident": injury_description,
            "legal_action": "API failed",
            "labor_law_section": "N/A",
            "error": str(e)
        }]







# # App/agent4_generator.py
# from App.agent3_lawresearch import research_similar_cases
# from App.agent2_report import generate_criminal_report

# def generate_final_output(extracted_data: dict) -> dict:
#     crime = extracted_data.get("crime", "")
#     location = extracted_data.get("location", "")

#     # Get report using your LLM
#     generated_report = generate_criminal_report(extracted_data)

#     # Get legal research results (via RAG)
#     similar_cases = research_similar_cases(crime, location)

#     # Final JSON output
#     output = {
#         "extracted_data": extracted_data,
#         "generated_report": generated_report,
#         "legal_research": {
#             "similar_cases": similar_cases,
#             "recommended_punishment": "Up to 3 years imprisonment or fine or both under Section 379",
#             "ppc_section": "379"
#         },
#         "ppc_section": "379"
#     }

#     return output


















# App/agent4_generator.py

from App.agent3_lawresearch import research_similar_injury_cases
from App.agent2_report import generate_injury_claim_report

def generate_final_output(extracted_data: dict) -> dict:
    injury_description = extracted_data.get("injury_description", "")
    incident_location = extracted_data.get("incident_location", "")

    # Generate a formal legal injury report using LLM
    generated_report = generate_injury_claim_report(extracted_data)

    # Retrieve legal research (similar cases, compensation, legal actions)
    similar_cases = research_similar_injury_cases(injury_description, incident_location)

    # Construct final JSON response
    output = {
        "extracted_data": extracted_data,
        "generated_report": generated_report,
        "legal_research": {
            "similar_cases": similar_cases,
            "recommended_action": "Compensation for medical expenses, paid leave, and safety policy revision",
            "relevant_laws": "Pakistan Labor Law, Workplace Safety and Welfare Act"
        }
    }

    return output

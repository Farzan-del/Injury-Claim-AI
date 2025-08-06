# def generate_criminal_report(extracted_info):
#     crime = extracted_info.get('crime', 'Unknown Crime')
#     location = extracted_info.get('location', 'Unknown Location')
#     name = extracted_info.get('name', 'Unknown Name')

#     report = (
#         f"Criminal Report for: {name}\n"
#         f"Crime Committed: {crime}\n"
#         f"Location of Crime: {location}\n"
#         f"Summary: The individual named {name} is accused of committing "
#         f"{crime} at {location}. Detailed investigation and legal review follows."
#     )
#     return report









# # agent2_report.py
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# import os
# from dotenv import load_dotenv

# # Load .env if using local file
# load_dotenv()

# # Create Gemini model instance
# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=0.3,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )

# # Define prompt template for report generation
# prompt = ChatPromptTemplate.from_template("""
# You are a legal expert. Write a formal criminal report based on the following extracted data:

# Name: {name}
# Crime: {crime}
# Location: {location}
# Date: {date}
# Additional Notes: {notes}

# The report should be 3-4 paragraphs long, using professional legal language.
# """)

# def generate_criminal_report(extracted_info):
#     # Extract input values
#     name = extracted_info.get('name', 'Unknown')
#     crime = extracted_info.get('crime', 'Unknown')
#     location = extracted_info.get('location', 'Unknown')
#     date = extracted_info.get('date', 'Unknown')
#     notes = extracted_info.get('additional notes', 'N/A')

#     # Format and run the prompt with Gemini
#     chain = prompt | llm
#     result = chain.invoke({
#         "name": name,
#         "crime": crime,
#         "location": location,
#         "date": date,
#         "notes": notes
#     })

#     return result.content  # Return LLM-generated report








# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# import os
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=0.3,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )

# prompt = ChatPromptTemplate.from_template("""
# You are a criminal law expert in Pakistan. Based on the extracted data below, write a comprehensive 3–4 paragraph formal criminal report in a professional legal tone.

# Include:
# - A summary of the crime and criminal details.
# - Mention of the location and date.
# - Legal interpretation and possible motive if evident.
# - Relevant section(s) of Pakistan Penal Code (PPC) if available.
# - Recommend legal action or punishment accordingly.

# Extracted Details:
# Name: {name}
# Crime: {crime}
# Location: {location}
# Date: {date}
# Additional Notes: {notes}
# """)

# def generate_criminal_report(extracted_info):
#     name = extracted_info.get('name', 'Unknown')
#     crime = extracted_info.get('crime', 'Unknown')
#     location = extracted_info.get('location', 'Unknown')
#     date = extracted_info.get('date', 'Unknown')
#     notes = extracted_info.get('additional notes', 'N/A')

#     chain = prompt | llm
#     result = chain.invoke({
#         "name": name,
#         "crime": crime,
#         "location": location,
#         "date": date,
#         "notes": notes
#     })

#     return result.content







from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

prompt = ChatPromptTemplate.from_template("""
You are a legal expert specializing in personal injury law and workplace compensation claims in Pakistan. Based on the extracted information below, draft a formal Personal Injury Claim Assessment Report in a clear, structured, and professional tone (3–4 paragraphs).

Include:
- A summary of the incident and injury.
- Important personal and incident details (dates, location, etc.).
- Legal interpretation based on workplace safety and injury compensation guidelines in Pakistan.
- Possible claim justification or recommendations for compensation.
- Mention any missing or ambiguous information if necessary.

Extracted Claim Form Details:
Full Name: {name}
Date of Birth: {dob}
Phone Number: {phone}
Email Address: {email}
Date of Incident: {incident_date}
Location of Incident: {incident_location}
Description of Injury: {injury_description}
Additional Notes: {additional_notes}
""")

def generate_injury_claim_report(extracted_info):
    name = extracted_info.get('name', 'Unknown')
    dob = extracted_info.get('dob', 'Unknown')
    phone = extracted_info.get('phone', 'Unknown')
    email = extracted_info.get('email', 'Unknown')
    incident_date = extracted_info.get('incident_date', 'Unknown')
    incident_location = extracted_info.get('incident_location', 'Unknown')
    injury_description = extracted_info.get('injury_description', 'Unknown')
    additional_notes = extracted_info.get('additional_notes', 'N/A')

    chain = prompt | llm
    result = chain.invoke({
        "name": name,
        "dob": dob,
        "phone": phone,
        "email": email,
        "incident_date": incident_date,
        "incident_location": incident_location,
        "injury_description": injury_description,
        "additional_notes": additional_notes
    })

    return result.content

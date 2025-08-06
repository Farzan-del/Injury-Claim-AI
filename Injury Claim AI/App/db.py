# import json
# from datetime import datetime
# import os

# def store_case(case_data):
#     filename = f"cases/case_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
#     os.makedirs("cases", exist_ok=True)

#     with open(filename, "w") as f:
#         json.dump(case_data, f, indent=4)

# # db.py
# from sqlalchemy import create_engine, Column, Integer, String, Text
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # SQLite database URL
# DATABASE_URL = "sqlite:///./cases.db"

# # Setup SQLAlchemy engine and session
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(bind=engine, autoflush=False)
# Base = declarative_base()

# # Define the Case model
# class LegalCase(Base):
#     __tablename__ = "legal_cases"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     crime = Column(String, nullable=False)
#     location = Column(String, nullable=False)
#     punishment = Column(String, nullable=False)
#     date = Column(String, nullable=True)
#     full_report = Column(Text, nullable=False)

# # Create the table (run once)
# Base.metadata.create_all(bind=engine)

# # Function to store a case
# def store_case(case_data):
#     session = SessionLocal()

#     # Get data from the response structure
#     name = case_data["extracted_data"].get("name", "Unknown")
#     crime = case_data["extracted_data"].get("crime", "Unknown")
#     location = case_data["extracted_data"].get("location", "Unknown")
#     date = case_data["extracted_data"].get("date", "N/A")
#     punishment = case_data["legal_research"].get("recommended_punishment", "N/A")
#     full_report = case_data["generated_report"]

#     # Create a new case record
#     new_case = LegalCase(
#         name=name,
#         crime=crime,
#         location=location,
#         punishment=punishment,
#         date=date,
#         full_report=full_report
#     )

#     # Add and commit to DB
#     session.add(new_case)
#     session.commit()
#     session.close()



from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL
DATABASE_URL = "sqlite:///./injury_claims.db"

# Setup SQLAlchemy engine and session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()

# Define the PersonalInjuryClaim model
class PersonalInjuryClaim(Base):
    __tablename__ = "injury_claims"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    dob = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    incident_location = Column(String, nullable=False)
    incident_date = Column(String, nullable=True)
    injury_description = Column(Text, nullable=False)
    recommended_action = Column(String, nullable=True)
    relevant_laws = Column(String, nullable=True)
    full_report = Column(Text, nullable=False)

# Create the table (run once)
Base.metadata.create_all(bind=engine)

# Function to store an injury claim
def store_injury_claim(case_data):
    session = SessionLocal()

    # Extract values from processed data
    extracted = case_data.get("extracted_data", {})
    legal_research = case_data.get("legal_research", {})

    new_claim = PersonalInjuryClaim(
        full_name=extracted.get("name", "Unknown"),
        dob=extracted.get("dob", "N/A"),
        phone=extracted.get("phone", "N/A"),
        email=extracted.get("email", "N/A"),
        incident_location=extracted.get("incident_location", "Unknown"),
        incident_date=extracted.get("incident_date", "N/A"),
        injury_description=extracted.get("injury_description", "N/A"),
        recommended_action=legal_research.get("recommended_action", "Pending evaluation"),
        relevant_laws=legal_research.get("relevant_laws", "Labor Law / Workplace Safety Act"),
        full_report=case_data.get("generated_report", "No report available.")
    )

    session.add(new_claim)
    session.commit()
    session.close()

# import streamlit as st
# import requests

# st.title("Legal Case Analyzer")

# uploaded_file = st.file_uploader("Upload a DOCX file", type=["docx"])

# if uploaded_file is not None:
#     if st.button("Analyze"):
#         with st.spinner("Analyzing..."):
#             files = {"file": (uploaded_file.name, uploaded_file, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")}

#             response = requests.post("http://127.0.0.1:8000/analyze-form/", files=files)

#             if response.status_code == 200:
#                 result = response.json()
#                 st.success("Analysis complete!")
#                 st.subheader("Extracted Data")
#                 st.json(result["extracted_data"])

#                 st.subheader("Generated Report")
#                 st.markdown(result["generated_report"])

#                 st.subheader("Legal Research")
#                 st.json(result["legal_research"])
#             else:
#                 st.error(f"Request failed with status {response.status_code}: {response.text}")




# # streamlit_app.py

# import streamlit as st
# import requests

# st.set_page_config(page_title="Legal Document Analyzer", layout="wide")
# st.title("⚖️ Legal Case Analyzer & RAG Assistant")

# tab1, tab2 = st.tabs(["📄 Upload & Analyze DOCX", "🧠 Ask Legal RAG Assistant"])

# # -----------------------------------------
# # TAB 1: DOCX UPLOAD & ANALYSIS
# # -----------------------------------------
# with tab1:
#     uploaded_file = st.file_uploader("Upload a Legal Case DOCX file", type=["docx"])

#     if uploaded_file:
#         if st.button("📊 Analyze Document"):
#             with st.spinner("Analyzing your document..."):
#                 files = {
#                     "file": (
#                         uploaded_file.name,
#                         uploaded_file,
#                         "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
#                     )
#                 }

#                 response = requests.post("http://127.0.0.1:8000/analyze-form/", files=files)

#                 if response.status_code == 200:
#                     result = response.json()

#                     st.success("✅ Analysis Complete!")
#                     st.subheader("📌 Extracted Data")
#                     st.json(result["extracted_data"])

#                     st.subheader("📝 Generated Criminal Report")
#                     st.markdown(result["generated_report"])

#                     st.subheader("📚 Legal Research Output")
#                     st.json(result["legal_research"])

#                     st.subheader("📕 Relevant PPC Section")
#                     st.code(result["ppc_section"])
#                 else:
#                     st.error(f"❌ Error {response.status_code}: {response.text}")

# # -----------------------------------------
# # TAB 2: RAG LEGAL ASSISTANT
# # -----------------------------------------
# with tab2:
#     st.markdown("Ask a question related to **Pakistan Penal Code** or criminal law context based on extracted cases.")
#     query = st.text_input("🧠 Ask a legal question (RAG-powered):")

#     if query:
#         if st.button("💬 Ask RAG Assistant"):
#             with st.spinner("Querying the RAG system..."):
#                 response = requests.post(
#                     "http://127.0.0.1:8000/ask_rag",
#                     params={"query": query}
#                 )

#                 if response.status_code == 200:
#                     answer = response.json()["answer"]
#                     st.success("🧠 Answer from RAG System:")
#                     st.markdown(f"**{answer}**")
#                 else:
#                     st.error(f"❌ Failed to get response: {response.status_code}")













# streamlit_app.py

# import streamlit as st
# import requests

# # --------------------
# # Page Config
# # --------------------
# st.set_page_config(
#     page_title="Legal Case Analyzer",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # --------------------
# # Header
# # --------------------
# st.markdown(
#     "<h2 style='text-align: center;'>⚖️ Legal Case Analyzer & Assistant</h2><hr>",
#     unsafe_allow_html=True
# )

# # --------------------
# # Tabs
# # --------------------
# tab1, tab2 = st.tabs(["📄 Upload & Analyze DOCX", "💬 Ask Legal Assistant"])

# # --------------------
# # TAB 1: Upload & Analyze DOCX
# # --------------------
# with tab1:
#     st.markdown("### 📂 Upload Your Legal Document")

#     uploaded_file = st.file_uploader("Upload a `.docx` legal case file", type=["docx"])

#     if uploaded_file:
#         if st.button("📊 Analyze Document", use_container_width=True):
#             with st.spinner("🔍 Analyzing document..."):
#                 files = {
#                     "file": (
#                         uploaded_file.name,
#                         uploaded_file,
#                         "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
#                     )
#                 }

#                 response = requests.post("http://127.0.0.1:8000/analyze-form/", files=files)

#                 if response.status_code == 200:
#                     result = response.json()

#                     with st.expander("📌 Extracted Information", expanded=True):
#                         st.json(result.get("extracted_data", {}))

#                     with st.expander("📝 Generated Criminal Report", expanded=True):
#                         st.markdown(result.get("generated_report", "_No report generated._"))

#                     with st.expander("📚 Legal Research Summary", expanded=False):
#                         st.json(result.get("legal_research", {}))

#                     with st.expander("📕 Relevant PPC Section", expanded=False):
#                         st.code(result.get("ppc_section", "N/A"))

#                     st.success("✅ Analysis Complete!")

#                 else:
#                     st.error(f"❌ Server Error ({response.status_code})")
#                     st.code(response.text)

# # --------------------
# # TAB 2: Ask Legal Assistant
# # --------------------
# with tab2:
#     st.markdown("### 🤖 Ask a Legal Question")
#     st.caption("Ask anything related to **Pakistan Penal Code** or your case context.")

#     query = st.text_input("Enter your legal query:")

#     if query:
#         if st.button("💬 Submit Query", use_container_width=True):
#             with st.spinner("🧠 Consulting RAG Legal Assistant..."):
#                 response = requests.post(
#                     "http://127.0.0.1:8000/ask_rag",
#                     params={"query": query}
#                 )

#                 if response.status_code == 200:
#                     answer = response.json().get("answer", "No answer returned.")
#                     st.success("📢 Response from RAG Assistant:")
#                     st.markdown(f"**{answer}**")
#                 else:
#                     st.error(f"❌ Server Error ({response.status_code})")
#                     st.code(response.text)











import streamlit as st
import requests

# --------------------
# Page Config
# --------------------
st.set_page_config(
    page_title="Personal Injury Claim Analyzer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------
# Header
# --------------------
st.markdown(
    "<h2 style='text-align: center;'>🩺 Personal Injury Claim Analyzer & Assistant</h2><hr>",
    unsafe_allow_html=True
)

# --------------------
# Tabs
# --------------------
tab1, tab2 = st.tabs(["📄 Upload & Analyze Claim Form", "💬 Ask Legal Assistant"])

# --------------------
# TAB 1: Upload & Analyze Claim Form
# --------------------
with tab1:
    st.markdown("### 📂 Upload Your Injury Claim Form (DOCX)")

    uploaded_file = st.file_uploader("Upload a `.docx` injury claim form", type=["docx"])

    if uploaded_file:
        if st.button("📊 Analyze Claim", use_container_width=True):
            with st.spinner("🔍 Analyzing claim form..."):
                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file,
                        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                }

                response = requests.post("http://127.0.0.1:8000/analyze-form/", files=files)

                if response.status_code == 200:
                    result = response.json()

                    with st.expander("📌 Extracted Claim Information", expanded=True):
                        st.json(result.get("extracted_data", {}))

                    with st.expander("📝 Generated Injury Report", expanded=True):
                        st.markdown(result.get("generated_report", "_No report generated._"))

                    with st.expander("📚 Legal Research Summary", expanded=False):
                        st.json(result.get("legal_research", {}))

                    st.success("✅ Injury Claim Analysis Complete!")

                else:
                    st.error(f"❌ Server Error ({response.status_code})")
                    st.code(response.text)

# --------------------
# TAB 2: Ask Legal Assistant
# --------------------
with tab2:
    st.markdown("### 🤖 Ask the Injury Claim Legal Assistant")
    st.caption("Ask anything related to **workplace injury laws**, **compensation**, or **claim rights** in Pakistan.")

    query = st.text_input("Enter your legal query:")

    if query:
        if st.button("💬 Submit Query", use_container_width=True):
            with st.spinner("🧠 Consulting RAG Assistant..."):
                response = requests.post(
                    "http://127.0.0.1:8000/ask_rag",
                    params={"query": query}
                )

                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer returned.")
                    st.success("📢 Legal Assistant Response:")
                    st.markdown(f"**{answer}**")
                else:
                    st.error(f"❌ Server Error ({response.status_code})")
                    st.code(response.text)

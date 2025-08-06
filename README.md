
## 🔷 GitHub Project Description (Short Summary for GitHub Repo)

> **Injury Claim AI** is an intelligent legal assistant designed to process personal injury claims. It uses Agentic AI to extract, analyze, and assess claim forms (PDF/DOCX), conduct legal research using Retrieval-Augmented Generation (RAG), and generate detailed claim assessment reports. Built with Python, FastAPI, Streamlit, Tesseract, PyMuPDF, Gemini (Google LLM), and vector stores (FAISS/ChromaDB), this system streamlines the personal injury claim process for employees and legal departments.


## 🚀 Features

- 📄 Upload PDF or DOCX injury claim forms
- 🧠 Automatic form extraction using OCR (Tesseract) and LLMs
- 📋 Claim analysis and expense validation
- ⚖️ Legal section matching (PPC or relevant laws)
- 🔍 Context-aware legal Q&A using RAG (Gemini + Chroma/FAISS)
- 📊 Auto-generated structured claim report
- 🤖 Agentic AI structure with task-specific agents and tools

---

## 🧱 Project Architecture

```

InjuryClaimAI/
├── App/
│   ├── api\_main.py            # FastAPI backend
│   ├── agents.py              # Agent definitions
│   ├── tools.py               # Tools: PDF/DOCX extractors, OCR, etc.
│   ├── tasks.py               # Tasks that agents execute
│   ├── llm\_config.py          # Gemini LLM configuration
│   ├── vector\_store.py        # FAISS or Chroma vector store
│   └── agent4\_rag.py          # RAG-based QA module
├── UI/
│   └── streamlit\_ui.py        # Streamlit-based frontend
├── data/
│   └── uploads/               # Uploaded files
├── requirements.txt
└── README.md

````

---

## 📦 Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **LLM**: Gemini via Google API
- **Document Extraction**: PyMuPDF (PDF), python-docx, Tesseract OCR
- **Vector Store**: FAISS or ChromaDB
- **Agent Framework**: Custom Agentic AI
- **Database (optional)**: SQLite or PostgreSQL

---

## 🧑‍💻 How It Works

1. **User Uploads** a claim form (PDF or DOCX).
2. **Agents** are triggered:
   - Extractor Agent: extracts form fields
   - Analyzer Agent: checks medical and expense info
   - Law Finder Agent: maps injury type to legal sections
   - RAG Agent: answers legal questions from claim context
3. **Tools** like OCR, LLM, and vector DBs are used accordingly.
4. **Report Generator** creates a final structured assessment report.
5. **Frontend** displays extracted content, legal analysis, and responses.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/injury-claim-ai.git
cd injury-claim-ai
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Ensure you have Tesseract installed:

* **Windows**: [https://github.com/tesseract-ocr/tesseract/wiki](https://github.com/tesseract-ocr/tesseract/wiki)
* **Linux**: `sudo apt install tesseract-ocr`

### 3. Add Environment Variables

Create a `.env` file:

```bash
GOOGLE_API_KEY=your_google_gemini_api_key
```

### 4. Run the Backend

```bash
uvicorn App.api_main:app --reload
```

### 5. Run the Frontend

```bash
streamlit run UI/streamlit_ui.py
```



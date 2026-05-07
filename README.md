# HR Document ChatBot Assistant

A Streamlit-based HR Policy chatbot that uses a RAG (Retrieval-Augmented Generation) pipeline to answer questions about uploaded HR policy documents.

## Features

- Upload HR policy PDFs
- Automatic document chunking and embedding via OpenAI
- Vector storage with ChromaDB for fast retrieval
- Context-aware answers grounded in the uploaded documents

## Prerequisites

- Python 3.11+
- An [OpenAI API key](https://platform.openai.com/api-keys)

## Setup

1. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv

   # macOS / Linux
   source venv/bin/activate

   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1

   # Windows (Command Prompt)
   venv\Scripts\activate.bat
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API key:**

   Create a `.env` file in the project root:

   ```
   OPENAI_API_KEY=sk-your-key-here
   ```

## Usage

```bash
streamlit run app.py
```

Open the URL shown in your terminal (default: http://localhost:8501), upload an HR policy PDF, click **Ingest/Process Document**, then ask questions.

To stop the app, press `Ctrl+C` in the terminal.

## Project Structure

```
app.py                  # Streamlit UI entry point
src/
  document_loaders.py   # PDF loading via PyMuPDF
  chunking.py           # Recursive text splitting
  embeddings.py         # OpenAI embedding model
  vectorstore.py        # ChromaDB vector store
  llm_integration.py    # ChatOpenAI LLM wrapper
  rag_pipeline.py       # Indexing and QA orchestration
prompts/
  prompt_template.py    # System/user prompt builder
config/
  config.yaml           # Centralised configuration values
data/sample_pdfs/       # Uploaded PDFs stored here
```

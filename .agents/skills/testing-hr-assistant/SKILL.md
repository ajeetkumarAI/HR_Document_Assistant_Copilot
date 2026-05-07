---
name: testing-hr-assistant
description: Test the HR Document Assistant Streamlit app end-to-end. Use when verifying UI, RAG pipeline, or error handling changes.
---

# Testing the HR Document Assistant

## Devin Secrets Needed

- `OPENAI_API_KEY` — Required for full end-to-end testing (document ingestion + QA). Without it, you can still test UI, error handling, and import correctness.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the Streamlit app:
   ```bash
   streamlit run app.py --server.headless true --server.port 8501
   ```

3. Open `http://localhost:8501` in Chrome.

## Tests That Work Without OPENAI_API_KEY

1. **App startup** — Verify the page loads with title, file uploader, question input, and "Get Answer" button.
2. **Empty question validation** — Click "Get Answer" with empty input. Expect yellow warning: "Please enter a question."
3. **No-documents guard** — Type a question and click "Get Answer" before ingesting any docs. Expect yellow warning: "No documents have been ingested yet..."
4. **File upload** — Upload a PDF via the uploader. Expect green success message and "Ingest/Process Document" button.
5. **Ingestion error handling** — Click "Ingest/Process Document" without API key. Expect red error box with credentials message (not an unhandled crash).
6. **Import check** — Run: `python -c "from src.rag_pipeline import indexing_pipeline, get_answer; print('OK')"`

## Full End-to-End Tests (Requires OPENAI_API_KEY)

1. Create a `.env` file with `OPENAI_API_KEY=sk-...`
2. Upload the included `data/sample_pdfs/HR-Policy.pdf`
3. Click "Ingest/Process Document" — should succeed with green message
4. Ask a question like "What is the leave policy?" — should return an answer with page citations
5. Restart the app and ask another question — vector store should persist (no re-ingestion needed)

## Notes

- The Streamlit file uploader requires Playwright for programmatic uploads:
  ```python
  from playwright.sync_api import sync_playwright
  with sync_playwright() as p:
      browser = p.chromium.connect_over_cdp("http://localhost:29229")
      page = [pg for pg in browser.contexts[0].pages if "8501" in pg.url][0]
      page.locator('input[type="file"]').set_input_files("/path/to/file.pdf")
  ```
- The `db/` directory is the ChromaDB persist directory. Delete it to reset the vector store.
- No linter or test suite is configured in this repo.

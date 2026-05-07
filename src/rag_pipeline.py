from src.document_loaders import load_documents
from src.chunking import chunk_documents
from src.embeddings import get_embedding_model
from src.vectorstore import create_vector_store, load_vector_store, get_retriever
from src.llm_integration import get_llm_model
from prompts.prompt_template import build_prompt

from dotenv import load_dotenv
import os   
load_dotenv()

def indexing_pipeline(file_path):
    # 1.Load documents
    documents = load_documents(file_path)

    # 2.Chunk documents
    chunks = chunk_documents(documents)

    # 3. Get embedding model
    embedding_model = get_embedding_model()

    # 4. Create vector store
    vector_store = create_vector_store(chunks, embedding_model)

    # 5. Persist vector store to disk
    vector_store.persist()

    # return vector store for immediate use
    return vector_store
   

def get_answer(question):
    # 1. Load embedding model
    embedding_model = get_embedding_model()

    # 2. Load vector store from disk
    vector_store = load_vector_store(embedding_model)

    # 3. Get retriever from vector store
    retriever = get_retriever(vector_store)

    # 4. Retrieve relevant context based on question
    relevant_docs = retriever.invoke(question)
    context ="\n\n".join([f"(Page {doc.metadata.get('page',"N/A")}) {doc.page_content}"  for doc in relevant_docs])  

    # 5. Build prompt for LLM
    prompt = build_prompt(context, question)

    # 6. Get LLM model
    llm = get_llm_model()

    # 7. Get answer from LLM
    response = llm.invoke(prompt)

    return response.content
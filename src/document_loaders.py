from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document


def load_documents(file_path: str) -> list[Document]:
    """Load pages from a PDF file and return them as LangChain Documents."""
    loader = PyMuPDFLoader(file_path)
    return loader.load()

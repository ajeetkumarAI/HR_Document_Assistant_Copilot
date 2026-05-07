from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(docs: list[Document]) -> list[Document]:
    """Split documents into smaller chunks for embedding."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=300,
        separators=["\n\n", "\n", "(?<=. )", " ", ""],
    )
    return text_splitter.split_documents(docs)

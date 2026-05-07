from langchain_community.document_loaders import PyMuPDFLoader


def load_documents(file_path:str):
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()
    return docs
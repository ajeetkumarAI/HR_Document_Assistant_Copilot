from langchain_community.vectorstores import Chroma

def create_vector_store(chunks, embeddings, persist_directory="db"):
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    return vector_store

def load_vector_store(embeddings, persist_directory="db"):
    vector_store = Chroma(
        embedding_function=embeddings,
        persist_directory=persist_directory
    )
    return vector_store


def get_retriever(vector_store):
    retriever = vector_store.as_retriever(
        search_type="mmr",                      # `mmr`: Maximal Marginal Relevance (Default: `similarity_score_threshold`) 
        search_kwargs={"k": 6}              # `k`: Amount of documents to return (Default: `4`)
    )
    return retriever


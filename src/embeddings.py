from langchain_openai import OpenAIEmbeddings


def get_embedding_model() -> OpenAIEmbeddings:
    """Return an OpenAI embedding model instance.

    The API key is read automatically from the OPENAI_API_KEY
    environment variable by the LangChain client.
    """
    return OpenAIEmbeddings(model="text-embedding-3-small")

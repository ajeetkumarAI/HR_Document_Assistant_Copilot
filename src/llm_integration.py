from langchain_openai import ChatOpenAI


def get_llm_model() -> ChatOpenAI:
    """Return a ChatOpenAI LLM instance.

    The API key is read automatically from the OPENAI_API_KEY
    environment variable by the LangChain client.
    """
    return ChatOpenAI(model_name="gpt-4o-mini", temperature=0)


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os   
load_dotenv()

def get_llm_model():
    llm = ChatOpenAI(model_name="gpt-5.4-nano-2026-03-17", temperature=0,openai_api_key=os.getenv("OPENAI_API_KEY"))
    return llm


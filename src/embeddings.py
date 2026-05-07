from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os   

load_dotenv()

def get_embedding_model():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    return embeddings

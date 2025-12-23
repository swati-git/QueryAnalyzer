from dotenv import load_dotenv
from langchain_cohere import ChatCohere
import os

load_dotenv()

api_key = os.getenv("COHERE_API_KEY")

llm_model  = ChatCohere(model="command-a-03-2025",temperature=0.2)
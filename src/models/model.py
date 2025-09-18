from langchain_google_generativeai import ChatGoogleGeneraiveAI
import os
from python_dotenv import load_dotenv

load_dotenv()

llm_model  = ChatGoogleGeneraiveAI(model="gemini-2.0-flash",
                              temperature=0.2)
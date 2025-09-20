from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

llm_model  = ChatGoogleGenerativeAI(model="gemini-2.0-flash",
                                    google_api_key=api_key,
                                    temperature=0.2)
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.agents.tools import tools
from src.log.logger import logger


load_dotenv()

# Check if API key is available
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    logger.error("GOOGLE_API_KEY environment variable is not set. Please set it in your .env file.")
    raise ValueError("GOOGLE_API_KEY environment variable is required")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    google_api_key=api_key
).bind_tools(tools)


summarizer = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.3,
    google_api_key=api_key
)
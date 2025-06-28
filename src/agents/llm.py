from langchain_google_genai import ChatGoogleGenerativeAI
from src.agents.tools import tools


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    max_tokens=1000
).bind_tools(tools)
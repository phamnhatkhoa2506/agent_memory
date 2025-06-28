import os
from dotenv import load_dotenv

from src.utils.redis_connection import connect_redis
from src.memory.search_index import create_search_index
from src.agents.tools import store_memory_tool, retrieve_memories_tool

load_dotenv()

if __name__ == "__main__":
    load_dotenv()
    print(retrieve_memories_tool.invoke({"query": "Airline preferences", "memory_types": ["episodic"]}))
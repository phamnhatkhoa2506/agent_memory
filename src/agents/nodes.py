from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.runnables.config import RunnableConfig
from src.agents.agent import travel_agent
from src.log.logger import logger
from src.agents.state import RuntimeState


def reponse_to_user(state: RuntimeState, config: RunnableConfig) -> RuntimeState:
    human_messages = [m for m in state if isinstance(m, HumanMessage)]
    if not human_messages:
        logger.warn("No human messages found!")
        return state
    
    try:
        result = travel_agent.invoke(
            {"messages": human_messages},
            config=config
        )

        ai_message = result["messages"][-1] 
        state["messages"].append(ai_message)
    except Exception as e:
        logger.error(f"Error invoking travel agent: {e}")

        ai_message = AIMessage(content="I'm sorry, I encountered an error processing your request.")
        state["messages"].append(ai_message)

    return state


def execute_tools(state: RuntimeState, config: RunnableConfig):
    ...


def summarize_conversation(state: RuntimeState, config: RunnableConfig):
    ...
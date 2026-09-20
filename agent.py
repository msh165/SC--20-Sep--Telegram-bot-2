from llm import groq_llm
from tools import live_cricket_score,live_football_score


from langchain.agents import create_agent


from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model=groq_llm,
    tools=[live_cricket_score,live_football_score],
    checkpointer=InMemorySaver(),
    system_prompt="""
    You are a helpful assistant
    When user asks for foootball score, tool live_football_scorez
    When user asks for cricket score, tool live_cricket_scorez
    """
)


# Configuration for memory (required by InMemorySaver)
config = {"configurable": {"thread_id": "1"}}
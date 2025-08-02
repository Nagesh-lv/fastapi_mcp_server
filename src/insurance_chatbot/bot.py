from langchain_ollama import ChatOllama
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp_use import MCPAgent
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

user_query = input("Enter your query: ")

sse_connection = {
    "transport": "sse",
    "url": "http://127.0.0.1:8000/mcp",
    "headers": None,
    "timeout": 30.0,
    "sse_read_timeout": 60.0,
    "session_kwargs": None,
    "httpx_client_factory": None,
}



llm = ChatOllama(model="gemma3:1b")
#tools = load_mcp_tools(session=None, connection=sse_connection)
#print("tools are", tools)
agent = MCPAgent(llm=llm, client=MultiServerMCPClient(connections=sse_connection))

async def chat():
    while True:
        user = input("You: ")
        if user.lower() in {"exit", "quit"}:
            break
        reply = await agent.run(user)
        print("Bot:", reply.)

if __name__ == "__main__":
    asyncio.run(chat())
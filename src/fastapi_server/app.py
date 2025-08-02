from fastapi import FastAPI
from src.fastapi_server.routes import knowledge_base_route
from fastapi_mcp import FastApiMCP

app = FastAPI()
mcp = FastApiMCP(app, include_operations=["get_insurance_docs"],name="insurance_docs_mcp_server", description="Insurance MCP server that retrieves data from the knowledge base and sends it to the LLM.")
app.include_router(knowledge_base_route.router)
mcp.mount()
mcp.setup_server()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.fastapi_server.app:app", host="0.0.0.0", port=8000)
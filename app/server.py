from mcp.server.fastmcp import FastMCP

# Tool regisztrációk
from app.tools.saucedemo_config_tool import saucedemo_config_tools
from app.tools.orangehrm_config_tool import orangehrm_config_tools

def create_server() -> FastMCP:
    """
    Create and configure the MCP server.
    All tools are registered here.
    """
    mcp = FastMCP(
        name="test-server",
        dependencies=[
            "playwright",
            "httpx",
            "beautifulsoup4",
        ]
    )

    # --- Register tool groups ---
    saucedemo_config_tools(mcp)
    orangehrm_config_tools(mcp)

    return mcp


# MCP entrypoint
mcp = create_server()

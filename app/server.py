import sys
from mcp.server.fastmcp import FastMCP

# Tool regisztrációk
from app.tools.browser_tools import register_browser_tools
from app.tools.auth_tools import register_auth_tools
from app.tools.cart_tools import register_cart_tools
from app.tools.checkout_tools import register_checkout_tools


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
    register_browser_tools(mcp)
    register_auth_tools(mcp)
    register_cart_tools(mcp)
    register_checkout_tools(mcp)

    return mcp


# MCP entrypoint
mcp = create_server()

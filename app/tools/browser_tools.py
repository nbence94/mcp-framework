import sys
from mcp.server.fastmcp import FastMCP
from app.browser.browser_manager import BrowserManager


def register_browser_tools(mcp: FastMCP):
    browser_manager = BrowserManager()

    @mcp.tool(
        name="OpenBrowser",
        description="Open a Chromium browser and navigate to the given URL. Keeps the browser open."
    )
    async def open_browser(url: str) -> str:
        try:
            result = await browser_manager.open(url)
            print(result, file=sys.stderr)
            return result
        except Exception as e:
            return f"FAIL: Error opening browser: {str(e)}"

    @mcp.tool(
        name="CloseBrowser",
        description="Close the currently open browser."
    )
    async def close_browser() -> str:
        try:
            result = await browser_manager.close()
            print(result, file=sys.stderr)
            return result
        except Exception as e:
            return f"FAIL: Error closing browser: {str(e)}"

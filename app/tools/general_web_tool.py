from app.capabilities.playwright_manager import PlaywrightManager


def general_web_tools(mcp):

    @mcp.tool(
        name="start_browser",
        description=(
            "Start a web browser session if not already running. "
            "Must be called before any navigation."
        )
    )
    async def start_browser(headless: bool = False):
        return await PlaywrightManager.start_browser(headless=headless)

    @mcp.tool(
        name="stop_browser",
        description="Stop the currently running web browser session."
    )
    async def stop_browser():
        return await PlaywrightManager.stop_browser()

    @mcp.tool(
        name="goto",
        description=(
            "Navigate the current browser page to the given URL. "
            "Requires that the browser is already started."
        )
    )
    async def goto(url: str):
        return await PlaywrightManager.goto(url)

    @mcp.tool(
        name="get_web_state",
        description="Get the current state of the web browser session."
    )
    async def get_web_state():
        return await PlaywrightManager.get_state()

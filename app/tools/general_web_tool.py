from app.capabilities.web.playwright_manager import PlaywrightManager
from app.core.logger import get_logger

log = get_logger("tool.general.web")


def general_web_tools(mcp):

    @mcp.tool(
        name="start_browser",
        description="Start a web browser session (Playwright)"
    )
    async def start_browser(headless: bool = False):
        log.info("Tool called: start_browser")
        return await PlaywrightManager.start_browser(headless=headless)

    @mcp.tool(
        name="stop_browser",
        description="Stop the currently running web browser session"
    )
    async def stop_browser():
        log.info("Tool called: stop_browser")
        return await PlaywrightManager.stop_browser()

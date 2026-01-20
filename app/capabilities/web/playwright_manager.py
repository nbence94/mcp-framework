from playwright.async_api import async_playwright
from app.states.web_state import WebState
from app.core.logger import get_logger

log = get_logger("capability.web.playwright")


class PlaywrightManager:

    @staticmethod
    async def start_browser(headless: bool = False) -> dict:
        if WebState.browser:
            log.info("Browser already running")
            return {"running": True, "started": False}

        log.info("Starting Playwright browser (async)")

        # ⬇⬇⬇ A LÉNYEG ⬇⬇⬇
        WebState.playwright_context = async_playwright()
        WebState.playwright = await WebState.playwright_context.__aenter__()

        WebState.browser = await WebState.playwright.chromium.launch(
            headless=headless
        )
        WebState.context = await WebState.browser.new_context()
        WebState.page = await WebState.context.new_page()

        log.info("Browser started")
        return {"running": True, "started": True}

    @staticmethod
    async def stop_browser() -> dict:
        if not WebState.browser:
            log.info("Browser not running")
            return {"running": False, "stopped": False}

        log.info("Stopping Playwright browser")

        try:
            if WebState.context:
                await WebState.context.close()
            if WebState.browser:
                await WebState.browser.close()
        finally:
            if WebState.playwright_context:
                await WebState.playwright_context.__aexit__(None, None, None)

            WebState.playwright = None
            WebState.playwright_context = None
            WebState.browser = None
            WebState.context = None
            WebState.page = None

        log.info("Browser stopped")
        return {"running": False, "stopped": True}

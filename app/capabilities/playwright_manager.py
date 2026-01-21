from playwright.async_api import async_playwright
from app.states.web_state import WebState


class PlaywrightManager:

    @staticmethod
    async def start_browser(headless: bool = False) -> dict:
        if WebState.browser:
            return {"running": True, "started": False}

        WebState.playwright = await async_playwright().start()
        WebState.browser = await WebState.playwright.chromium.launch(
            headless=headless
        )
        WebState.context = await WebState.browser.new_context()
        WebState.page = await WebState.context.new_page()

        return {"running": True, "started": True}

    @staticmethod
    async def stop_browser() -> dict:
        if not WebState.browser:
            return {"running": False, "stopped": False}

        if WebState.context:
            await WebState.context.close()
        if WebState.browser:
            await WebState.browser.close()
        if WebState.playwright:
            await WebState.playwright.stop()

        WebState.playwright = None
        WebState.browser = None
        WebState.context = None
        WebState.page = None

        return {"running": False, "stopped": True}

    @staticmethod
    async def goto(url: str) -> dict:
        if not WebState.page:
            return {
                "error": "Browser not started"
            }

        await WebState.page.goto(url)

        return {
            "status": "navigated",
            "url": url
        }


    @staticmethod
    async def get_state() -> dict:
        return {
            "browser_running": WebState.browser is not None,
            "has_page": WebState.page is not None,
            "current_url": WebState.page.url if WebState.page else None
        }

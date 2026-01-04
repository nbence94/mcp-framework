from playwright.async_api import async_playwright
from app.state import state

class BrowserManager:

    async def open(self, url: str):
        if state.browser:
            return "Browser already open"

        state.playwright = await async_playwright().start()
        state.browser = await state.playwright.chromium.launch(headless=False)
        state.context = await state.browser.new_context()
        state.page = await state.context.new_page()

        await state.page.goto(url)
        return f"Browser opened at {url}"

    async def close(self):
        if not state.browser:
            return "No browser open"

        await state.context.close()
        await state.browser.close()
        await state.playwright.stop()

        state.page = None
        state.context = None
        state.browser = None
        state.playwright = None

        return "Browser closed"

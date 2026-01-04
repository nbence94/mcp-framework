from playwright.async_api import Browser, BrowserContext, Page, Playwright

class AppState:
    playwright: Playwright | None = None
    browser: Browser | None = None
    context: BrowserContext | None = None
    page: Page | None = None

state = AppState()

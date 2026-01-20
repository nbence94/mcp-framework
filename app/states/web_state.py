from typing import Optional
from playwright.async_api import Playwright, Browser, BrowserContext, Page


class WebState:
    playwright: Optional[Playwright] = None
    browser: Optional[Browser] = None
    context: Optional[BrowserContext] = None
    page: Optional[Page] = None

    @classmethod
    def is_running(cls) -> bool:
        return cls.browser is not None

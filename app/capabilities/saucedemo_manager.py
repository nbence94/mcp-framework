from app.states.web_state import WebState


class SaucedemoLoginPage:
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"

    HAMBURGER_BTN = "#react-burger-menu-btn"
    LOGOUT_BTN = "#logout_sidebar_link"

    @staticmethod
    async def login(username: str, password: str):
        if not WebState.page:
            raise RuntimeError(
                "No active page in WebState. Did you start the browser?"
            )

        await WebState.page.fill(SaucedemoLoginPage.USERNAME, username)
        await WebState.page.fill(SaucedemoLoginPage.PASSWORD, password)
        await WebState.page.click(SaucedemoLoginPage.LOGIN_BTN)

    @staticmethod
    async def logout():
        if not WebState.page:
            raise RuntimeError(
                "No active page in WebState. Did you start the browser?"
            )

        await WebState.page.click(SaucedemoLoginPage.HAMBURGER_BTN)
        await WebState.page.click(SaucedemoLoginPage.LOGOUT_BTN)

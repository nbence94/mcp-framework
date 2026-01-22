from app.states.web_state import WebState


class OrangeHrmManager:
    USERNAME = "xpath=//input[@name='username']"
    PASSWORD = "xpath=//input[@name='password']"
    LOGIN_BTN = "xpath=//button[@type='submit']"

    HAMBURGER_BTN = "xpath=//li[@class='oxd-userdropdown']"
    LOGOUT_BTN = "xpath=//a[text()='Logout']"

    @staticmethod
    async def login(username: str, password: str):
        if not WebState.page:
            raise RuntimeError(
                "No active page in WebState. Did you start the browser?"
            )

        await WebState.page.fill(OrangeHrmManager.USERNAME, username)
        await WebState.page.fill(OrangeHrmManager.PASSWORD, password)
        await WebState.page.click(OrangeHrmManager.LOGIN_BTN)

    @staticmethod
    async def logout():
        if not WebState.page:
            raise RuntimeError(
                "No active page in WebState. Did you start the browser?"
            )

        await WebState.page.click(OrangeHrmManager. HAMBURGER_BTN)
        await WebState.page.click(OrangeHrmManager.LOGOUT_BTN)

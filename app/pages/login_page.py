from app.state import state

class LoginPage:

    async def login(self, username: str, password: str):
        page = state.page
        if not page:
            raise RuntimeError("No active page")

        await page.goto("https://www.saucedemo.com/")
        await page.fill("#user-name", username)
        await page.fill("#password", password)
        await page.click("#login-button")

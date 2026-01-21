from app.capabilities.saucedemo_manager import SaucedemoLoginPage


def saucedemo_web_tools(mcp):

    @mcp.tool(
        name="login_saucedemo",
        description=(
            "Login to Saucedemo using a configured user. "
            "Requires that the browser is already started."
        )
    )
    async def login_saucedemo(username: str, password: str):

        await SaucedemoLoginPage.login(username, password)

        return {
            "status": "login_attempted",
            "user": username
        }

    @mcp.tool(
        name="logout_saucedemo",
        description=(
            "Logout from Saucedemo. "
            "Requires that the browser is already started."
        )
    )
    async def logout_saucedemo():

        await SaucedemoLoginPage.logout()

        return {
            "status": "logout_attempted"
        }

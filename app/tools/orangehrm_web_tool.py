from app.capabilities.orangehrm_manager import OrangeHrmManager


def orangehrm_web_tools(mcp):

    @mcp.tool(
        name="login_orangehrm",
        description=(
            "Login to OrangeHRM using a configured user. "
            "Requires that the browser is already started."
        )
    )
    async def login_orangehrm(username: str, password: str):

        await OrangeHrmManager.login(username, password)

        return {
            "status": "login_attempted",
            "user": username
        }

    @mcp.tool(
        name="logout_orangehrm",
        description=(
            "Logout from OrangeHRM. "
            "Requires that the browser is already started."
        )
    )
    async def logout_orangehrm():

        await OrangeHrmManager.logout()

        return {
            "status": "logout_attempted"
        }

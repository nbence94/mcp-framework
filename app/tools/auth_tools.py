from mcp.server.fastmcp import FastMCP
from app.pages.login_page import LoginPage

def register_auth_tools(mcp: FastMCP):

    @mcp.tool(
        name="LoginToSauceDemo",
        description="Login to Sauce Demo with standard user"
    )
    async def login() -> str:
        page = LoginPage()
        await page.login("standard_user", "secret_sauce")
        return "Logged in successfully"

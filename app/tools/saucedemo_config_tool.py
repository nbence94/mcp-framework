from app._config.readers.saucedemo import SaucedemoConfig

def saucedemo_config_tools(mcp):

    config = SaucedemoConfig()

    @mcp.tool(
        name="saucedemo_list_users",
        description="List all available Saucedemo users from config"
    )
    def list_users():
        return config.users()

    @mcp.tool(
        name="saucedemo_get_user",
        description="Get one Saucedemo user from config"
    )
    def get_user(username: str):
        return config.user(username)

    @mcp.tool(
        name="saucedemo_base_url",
        description="Get Saucedemo base URL"
    )
    def base_url():
        return config.base_url()

    @mcp.tool(
        name="saucedemo_default_user",
        description="Get default Saucedemo user"
    )
    def default_user():
        return config.default_user()

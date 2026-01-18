from app._config.readers.orangehrm import OrangeHrmConfig

def orangehrm_config_tools(mcp):

    config = OrangeHrmConfig()

    @mcp.tool(
        name="orangehrm_list_users",
        description="List all available OrangeHRM users from config"
    )
    def list_users():
        return config.users()

    @mcp.tool(
        name="orangehrm_get_user",
        description="Get one OrangeHRM user from config"
    )
    def get_user(username: str):
        return config.user(username)

    @mcp.tool(
        name="orangehrm_base_url",
        description="Get OrangeHRM base URL"
    )
    def base_url():
        return config.base_url()

    @mcp.tool(
        name="orangehrm_default_user",
        description="Get default OrangeHRM user"
    )
    def default_user():
        return config.default_user()

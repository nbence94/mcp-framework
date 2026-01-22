from pathlib import Path
from app.core.yaml_config import YamlConfig
from app.core.logger import get_logger
from app.core.env import get_env

class OrangeHrmConfig:

    def __init__(self):
        self.log = get_logger("config.orangehrm")

        self._base_dir = Path(__file__).parents[2] / "_config"
        self.log.debug("Config base dir: %s", self._base_dir)

        self._yaml = YamlConfig(self._base_dir)

        self.log.info("Loading orangehrm.yaml")
        self._data = self._yaml.load("apps/orangehrm.yaml")

        self.log.info(
            "Loaded OrangeHRM config: %d users",
            len(self._data.get("auth", {}).get("users", {}))
        )

    # -------- infra --------

    def base_dir(self):
        return self._base_dir

    # -------- domain API --------

    def base_url(self):
        url = self._data["app"]["base_url"]
        self.log.debug("Base URL requested: %s", url)
        return url

    def users(self):
        users = self._data["auth"]["users"]
        self.log.debug("Users requested: %s", list(users.keys()))
        return users

    def user(self, key: str) -> dict:
        user = self._data["auth"]["users"].get(key)

        if not user:
            raise KeyError(f"Unknown OrangeHRM user: {key}")

        password_env = user["password_env"]
        password = get_env(password_env)

        self.log.info("Resolved credentials for user: %s", key)

        return {
            "username": user["username"],
            "password": password,
        }

    def default_user(self):
        default = self._data["auth"]["default_user"]
        self.log.debug("Default user requested: %s", default)
        return default







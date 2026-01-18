import yaml
from pathlib import Path

class YamlConfig:
    _cache = {}

    def __init__(self, base_dir: Path):
        self.base_dir = base_dir

    def load(self, relative_path: str) -> dict:
        full_path = self.base_dir / relative_path

        if not full_path.exists():
            raise FileNotFoundError(full_path)

        if full_path not in self._cache:
            with open(full_path, "r", encoding="utf-8") as f:
                self._cache[full_path] = yaml.safe_load(f) or {}

        return self._cache[full_path]

    def reload(self, relative_path: str):
        full_path = self.base_dir / relative_path
        self._cache.pop(full_path, None)
        return self.load(relative_path)

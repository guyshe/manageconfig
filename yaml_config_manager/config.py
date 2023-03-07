import yaml
from typing import Dict
from pathlib import Path


class YamlConfig:
    def __init__(self, config_items: Dict) -> None:
        for key, value in config_items.items():
            attr_value = YamlConfig(value) if isinstance(value, dict) else value
            self.__setattr__(key, attr_value)
    
    @staticmethod
    def load_from_file(path: Path):
        with open(path) as f:
            return YamlConfig(yaml.load(f, Loader=yaml.FullLoader))


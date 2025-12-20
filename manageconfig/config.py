import yaml
import json
from typing import Dict
from pathlib import Path


class Config:
    def __init__(self, config_items: Dict) -> None:
        for key, value in config_items.items():
            attr_value = Config(value) if isinstance(value, dict) else value
            self.__setattr__(key, attr_value)

    @staticmethod
    def load_from_yml(path: Path):
        with open(path) as f:
            return Config(yaml.safe_load(f))

    @staticmethod
    def load_from_json(path: Path):
        with open(path) as f:
            return Config(json.load(f))

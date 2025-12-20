from pathlib import Path
from manageconfig import Config

JSON_FILE = Path(Path(__file__).parent, "config.json")


def test_sanity():
    conf = Config.load_from_json(JSON_FILE)

    assert conf.version == "1.0.0"
    assert conf.dependencies == ["express", "body-parser", "mongodb"]
    assert conf.scripts.start == "node app.js"
    assert isinstance(conf.numberKey, int)
    assert conf.numberKey == 123
    assert not conf.private


def test_nested_types():
    conf = Config.load_from_json(JSON_FILE)

    assert isinstance(conf.scripts, Config)
    assert isinstance(conf.dependencies, list)

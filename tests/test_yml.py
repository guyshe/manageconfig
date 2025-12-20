from pathlib import Path
from manageconfig import Config

YAML_FILE = Path(Path(__file__).parent, "config.yml")


def test_sanity():
    conf = Config.load_from_yml(YAML_FILE)

    assert conf.key == "value"
    assert conf.mysqldatabase.hostname == "localhost"
    assert isinstance(conf.mysqldatabase.port, int)
    assert not conf.booleanValue


def test_nested_types():
    conf = Config.load_from_yml(YAML_FILE)

    assert isinstance(conf.mysqldatabase, Config)
    assert isinstance(conf.arraylist, list)
    assert conf.arraylist[0] == "One"

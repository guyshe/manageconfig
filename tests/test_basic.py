from pathlib import Path
from manageconfig import Config

YAML_FILE = Path(Path(__file__).parent, 'config.yml')

def test_sanity():
    conf = Config.load_from_yml(YAML_FILE)

    assert conf.key == 'value'
    assert conf.mysqldatabase.hostname == 'localhost'
    assert type(conf.mysqldatabase.port) == int
    assert not conf.booleanValue
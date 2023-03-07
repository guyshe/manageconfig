from pathlib import Path
from yaml_config_manager import YamlConfig

YAML_FILE = Path(Path(__file__).parent, 'config.yml')

def test_sanity():
    conf = YamlConfig.load_from_file(YAML_FILE)

    assert conf.key == 'value'
    assert conf.mysqldatabase.hostname == 'localhost'
    assert type(conf.mysqldatabase.port) == int
    assert not conf.booleanValue
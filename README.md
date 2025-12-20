# ManageConfig

[![PyPI](https://img.shields.io/pypi/v/manageconfig)](https://pypi.org/project/manageconfig/)
[![Python](https://img.shields.io/pypi/pyversions/manageconfig)](https://pypi.org/project/manageconfig/)
[![License](https://img.shields.io/pypi/l/manageconfig)](https://github.com/guyshe/manageconfig/blob/main/LICENSE)

Tiny, practical config loader that turns JSON and YAML into dot-access objects.
Designed for scripts, CLIs, and small services that want clean config access
without a heavy dependency tree.

## Highlights

- Dot access for nested config values (`conf.db.host`)
- JSON and YAML support with a single API
- Lightweight, no magic beyond clean attribute access
- Friendly to scripts and small apps

## Install

```bash
pip install manageconfig
```

## Quickstart

```python
from manageconfig import Config

conf = Config.load_from_yml("config.yml")

print(conf.string2)
print(conf.string1)

# Prints "localhost"
print(conf.mysqldatabase.hostname)

# i == 3013
i = conf.mysqldatabase.port + 1
```

## Use Cases

- Project settings loaded once and reused across modules
- Local dev secrets and per-environment configuration
- Lightweight config handling in CLI tools

## Example Config (YAML)

```yml
# comment syntax

# basic syntax - key and value separated by colon and space before the value
key: value

# Scalar data types
integerValue: 1                     # integer value
floatingValue: 1                     # floating value

stringValue: "456"                  # string with double quotes
stringValue: 'abc'                   # string with single quotes
stringValue: wer                     # string without quotes

booleanValue: true                   # boolean values - true or false

# Multiline string with literal block syntax - preserved new lines
string1: |
  Line1
  line2
  "line3"
  line4

# Multiline strings with folded block syntax - new lines are not preserved,
# leading and trailing spaces are ignored
string2: >
  Line1
  line2
  "line3"
  line4

# Collection sequence data types
arraylist:
  - One
  - two
  - Three

arraylist2: [one, two , three]

mysqldatabase:
  hostname: localhost
  port: 3012
  username: root
  password: root
```

## JSON Support

Use `Config.load_from_json("config.json")`.

## API

- `Config.load_from_yml(path)` loads YAML into a dot-access object
- `Config.load_from_json(path)` loads JSON into a dot-access object

## Testing

```bash
tox
```

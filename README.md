# config manager

### Installation:
```
pip install manageconfig
```

This library manages config files and exposes them as Python objects. It is super small, basic, and easy to use.

**Note:** This package currently supports only YAML configurations, but we will add support for other formats soon (and we are open to suggestions).

## Example:

Suppose we want to load the `config.py` file attached below. We can do it as follows:


```python
from manageconfig import Config

conf = Config.load_from_yml('config.yml')

print(conf.string2)
print(conf.string1)

# This will print 'localhost'
print(conf.mysqldatabase.hostname)

# i == 3013
i = conf.mysqldatabase.port + 1

```



```yml

# comment syntax

# basic syntax - key and value separated by colon and space before the value
key: value

# Scalar data types
integerValue: 1                     # integer value
floatingValue: 1                     # floating vale

stringValue: "456"                   # string with double quotes
stringValue: 'abc'                  # string with single quotes
stringValue: wer                   # string without quotes

booleanValue: true                   # boolean values - true or false


# Multiline string with literal block syntax -preserved new lines
string1: |
  Line1
  line2
  "line3"
  line4

# Multiline strings with folded block syntax - new lines are not preserved, leading and trailing spaces are ignore
string2: >
  Line1
  line2
  "line3"
  line4
# Collection sequence data types
# sequence arraylist example
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



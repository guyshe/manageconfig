# Yaml config manager

loads yaml config file and expose it as python object.
This library is super small, basic, and easy to use

## Example:

Suppose we want to load the `config.py` file attached below, 
we will do it as follows:


```python
from yaml_config_manager import YamlConfig

conf = YamlConfig.load_from_yml('config.yml')

print(conf.string2)
print(conf.string1)

# will print 'localhost'
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



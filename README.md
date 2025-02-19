# Get value from nested JSON object
This repository contains:
- get_json_value.py
- demo.sh
- exmaple_result.png

# get_json_value.py
This python script get two arguments from user, the JSON object and the key.
The script get value from the JSON object according to the JSON key.

```javascript I'm A tab
python3 get_json_value.py <JSON_OBJECT> <JSON_KEY_TO_VALIDATE_VALUE>

python3 get_json_value.py {"a":{"b":{"c":"d"}}} a/b/c
```

# demo.sh and exmaple_result.png
This shell script demonstrate get_json_value.py usage.
and the output as shown in exmaple_result.png
```javascript I'm A tab
sh demo.sh
```
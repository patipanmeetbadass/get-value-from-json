#!/bin/bash

# Vars
PYTHON_SCRIPT_FILE="get_json_value.py"

# Test cases
TEST_CASES=(
    '{"a":{"b":{"c":"d"}}}' "a/b/c"
    '{"x":{"y":{"z":{"w":"value"}}}}' "x/y/z"
    '{"nested":{"level1":{"level2":{"level3":{"level4":"final_value"}}}}}' "nested/level1/level2/level3/level4"
)

# Demo
for ((i=0; i<${#TEST_CASES[@]}; i+=2)); do
    JSON_OBJECT=${TEST_CASES[i]}
    KEY_PATH=${TEST_CASES[i+1]}
    
    echo "Testing JSON: $JSON_OBJECT"
    echo "Key Path: $KEY_PATH"
    
    # Execute python script with arguments
    python3 ${PYTHON_SCRIPT_FILE} "$JSON_OBJECT" "$KEY_PATH"
    
    echo "--------------------------------------"
done

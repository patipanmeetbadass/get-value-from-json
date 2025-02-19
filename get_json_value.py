# Import the json module to handle JSON data
# Import sys to read command-line arguments
import json
import sys

def get_nested_value(json_data, json_input_key):
    """
    Get a nested value from a dictionary using a path.
    json_input_object_data: The dictionary containing nested JSON data.
    json_input_key: The key path in the format 'a/b/c'.
    return: The value at the specified path or None if not found.
    """
    keys = json_input_key.strip('/').split('/')
    for key in keys:
        if isinstance(json_data, dict) and key in json_data:
            json_data = json_data[key]
        else:
            # Handle key path not found
            return None
    return json_data

if __name__ == "__main__":
    # Validate inputs for two arguments
    if len(sys.argv) != 3:
        print("Usage: python3 nested_json_parser.py '<JSON_OBJECT>' '<JSON_KEY_TO_VALIDATE_VALUE>'")
        exit(1)

    # Get JSON input from user
    # First argument: JSON object as a string
    # Second argument: Key path
    json_input_object = sys.argv[1]
    json_input_key = sys.argv[2]

    try:
        # Parse JSON string into a dictionary
        json_data = json.loads(json_input_object)
    except json.JSONDecodeError:
        print("Invalid JSON input.")
        exit(1)

    result = get_nested_value(json_data, json_input_key)
    
    print(f"Input: {json_input_key}")
    print(f"Value: {json.dumps(result, indent=4) if result is not None else 'Key not found'}")

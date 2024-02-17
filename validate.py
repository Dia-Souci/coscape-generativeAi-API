import json

def is_json(json_string: str):
    try:
        json.loads(json_string)
    except json.decoder.JSONDecodeError:
        return False
    return True
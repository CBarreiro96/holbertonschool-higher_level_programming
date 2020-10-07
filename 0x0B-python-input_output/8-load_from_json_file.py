#!/usr/bin/python3
def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""

    with open(filename, 'w', encoding="utf-8") as f:
        return json.loads(f)

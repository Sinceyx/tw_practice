import json


def read_json_file(file_path):
    text = ''
    with open(file_path, "r") as f:
        text += f.read()
    return json.loads(text)

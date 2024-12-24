import json


def load_annotations(path):
    with open(path, "r") as f:
        return json.load(f)

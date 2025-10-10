#!/usr/bin/python3
"""task_00_basic_serialization

Serialize a Python dictionary to JSON and deserialize JSON to a Python dict.
"""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize `data` (a dict) to JSON and save it to `filename`.

    If the file exists it is replaced.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON from `filename` and return the corresponding Python dict.

    If the file can't be opened or the content is invalid JSON,
    the exception will propagate (caller can handle it). Returns the dict.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

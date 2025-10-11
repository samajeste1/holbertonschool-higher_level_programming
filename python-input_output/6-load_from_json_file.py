#!/usr/bin/python3
"""Load a Python object from a JSON file."""

import json

def load_from_json_file(filename):
    """Return the Python object represented in JSON file filename.

    Args:
        filename: path to JSON file

    Returns:
        object: Python object loaded from file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

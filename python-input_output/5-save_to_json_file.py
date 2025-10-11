#!/usr/bin/python3
"""Save a Python object to a file as JSON."""

import json

def save_to_json_file(my_obj, filename):
    """Write JSON representation of my_obj to filename.

    Args:
        my_obj: JSON-serializable Python object
        filename: file path to write
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

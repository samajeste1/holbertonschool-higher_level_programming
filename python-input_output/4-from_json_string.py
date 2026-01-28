#!/usr/bin/python3
"""Convert a JSON string to a Python object."""

import json


def from_json_string(my_str):
    """Return Python object represented by JSON string my_str.

    Args:
        my_str (str): JSON string

    Returns:
        object: deserialized Python object
    """
    return json.loads(my_str)

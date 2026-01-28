#!/usr/bin/python3
"""Convert a Python object to its JSON string representation."""

import json


def to_json_string(my_obj):
    """Return JSON representation (string) of my_obj.

    Args:
        my_obj: object serializable by json

    Returns:
        str: JSON string
    """
    return json.dumps(my_obj)

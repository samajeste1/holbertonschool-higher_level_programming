#!/usr/bin/python3
"""Return the dictionary representation of an object for JSON serialization."""

def class_to_json(obj):
    """Return a dict containing simple data structure (list, dict, str, int, bool)
    for JSON serialization of obj.

    Only instance attributes (from obj.__dict__) are included.
    """
    return dict(obj.__dict__)

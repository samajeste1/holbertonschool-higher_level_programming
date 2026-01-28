#!/usr/bin/python3
"""Return dict representation of an object for JSON serialization."""


def class_to_json(obj):
    """Return a dict for JSON serialization of obj.

    Only instance attributes (from obj.__dict__) are included.
    """
    return dict(obj.__dict__)

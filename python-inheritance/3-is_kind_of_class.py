#!/usr/bin/python3
"""Module 3-is_kind_of_class
Defines a function to check if an object is instance of a class.
"""


def is_kind_of_class(obj, a_class):
    """Return True if ``obj`` is an instance of ``a_class`` or its parents."""
    return isinstance(obj, a_class)

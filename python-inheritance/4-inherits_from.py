#!/usr/bin/python3
"""Module 4-inherits_from
Defines a function to test if an object is a strictly inherited instance.
"""


def inherits_from(obj, a_class):
    """Return True if ``obj`` is an instance of a subclass of ``a_class``."""
    return isinstance(obj, a_class) and type(obj) is not a_class

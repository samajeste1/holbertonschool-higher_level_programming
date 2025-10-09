#!/usr/bin/python3
"""
Module 0-add_integer
Contains one function add_integer(a, b=98)
that returns the addition of a and b.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats after casting to int.
    Raises:
        TypeError: if a or b are not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

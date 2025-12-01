#!/usr/bin/python3
"""Module 7-base_geometry
Defines class ``BaseGeometry`` with validation helpers.
"""


class BaseGeometry:
    """Geometry base class with area and integer validation."""

    def area(self):
        """Raise an exception because area is not defined here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that ``value`` is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")



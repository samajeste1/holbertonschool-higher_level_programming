#!/usr/bin/python3
"""Module 6-base_geometry
Defines class ``BaseGeometry`` with an unimplemented area method.
"""


class BaseGeometry:
    """Geometry base class with abstract area method."""

    def area(self):
        """Raise an exception because area is not defined here."""
        raise Exception("area() is not implemented")

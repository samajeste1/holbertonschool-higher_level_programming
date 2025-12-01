#!/usr/bin/python3
"""Module 9-rectangle
Defines class ``Rectangle`` with area and string representation.
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle defined by width and height."""

    def __init__(self, width, height):
        """Initialize rectangle with validated private width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Return formal string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"



#!/usr/bin/python3
"""Module 10-square
Defines class ``Square`` that inherits from ``Rectangle``.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square defined by size."""

    def __init__(self, size):
        """Initialize square with validated private size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return square area."""
        return self.__size * self.__size



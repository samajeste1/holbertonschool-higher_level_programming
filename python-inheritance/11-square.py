#!/usr/bin/python3
"""Module 11-square
Defines class ``Square`` that inherits from ``Rectangle`` with custom print.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square defined by size with custom string representation."""

    def __init__(self, size):
        """Initialize square with validated private size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return square area."""
        return self.__size * self.__size

    def __str__(self):
        """Return string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"



#!/usr/bin/python3
"""3-square module.

Adds area() method to Square.
"""


class Square:
    """Square class with size validation and an area() method."""

    def __init__(self, size=0):
        """Initialize a Square with validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

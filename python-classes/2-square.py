#!/usr/bin/python3
"""2-square module.

Defines a Square with size validation on construction.
"""


class Square:
    """Square class that validates size at instantiation."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int): size of the square (must be integer >= 0)
        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

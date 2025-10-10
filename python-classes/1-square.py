#!/usr/bin/python3
"""1-square module.

Defines a Square with a private size attribute.
"""


class Square:
    """Square class with a private size attribute.

    The size is stored as a private attribute: __size.
    """

    def __init__(self, size):
        """Initialize a Square with given size (no validation here)."""
        self.__size = size

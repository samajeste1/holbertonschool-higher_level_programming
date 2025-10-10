#!/usr/bin/python3
"""4-square module.

Adds property getter and setter for size with validation.
"""


class Square:
    """Square with size property (getter/setter) and area method."""

    def __init__(self, size=0):
        """Initialize a Square with validated size."""
        self.size = size  # will use the setter for validation

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): new size
        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

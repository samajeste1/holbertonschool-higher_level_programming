#!/usr/bin/python3
"""6-square module.

Adds position attribute to Square to print with offsets.
"""


class Square:
    """Square with size and position, area and printing methods."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square.

        Args:
            size (int): size of the square (validated)
            position (tuple): (x_offset, y_offset) both ints >= 0 (validated)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation.

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation.

        Position must be a tuple of 2 positive integers.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' with respect to position.

        position[1] is the number of newlines before the square (vertical offset).
        position[0] is the number of spaces before each printed line (horizontal offset).
        If size == 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # vertical offset
        for _ in range(self.__position[1]):
            print()

        # each printed line has horizontal offset spaces then the hashes
        space_prefix = " " * self.__position[0]
        for _ in range(self.__size):
            print(f"{space_prefix}{'#' * self.__size}")

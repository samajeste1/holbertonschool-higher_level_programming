#!/usr/bin/python3
"""task_01_duck_typing

Defines Shape ABC and concrete Circle and Rectangle classes.
Provides shape_info() that uses duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract shape interface requiring area and perimeter methods."""

    @abstractmethod
    def area(self):
        """Return area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle defined by its radius."""

    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Return area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle defined by width and height."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Print area and perimeter of obj using duck typing.

    The function assumes that obj implements .area() and .perimeter().
    """
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))

#!/usr/bin/python3
"""task_00_abc

Defines an abstract Animal class and concrete subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound produced by the animal."""
        pass


class Dog(Animal):
    """Concrete Dog class."""

    def sound(self):
        """Return dog sound."""
        return "Bark"


class Cat(Animal):
    """Concrete Cat class."""

    def sound(self):
        """Return cat sound."""
        return "Meow"

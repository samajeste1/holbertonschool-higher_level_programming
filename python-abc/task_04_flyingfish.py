#!/usr/bin/python3
"""task_04_flyingfish

Demonstrates multiple inheritance and method overriding with FlyingFish.
"""


class Fish:
    """Simple Fish class."""

    def swim(self):
        """Print swimming behaviour."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat."""
        print("The fish lives in water")


class Bird:
    """Simple Bird class."""

    def fly(self):
        """Print flying behaviour."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish inherits from Fish and Bird and overrides behaviors."""

    def fly(self):
        """Override fly for FlyingFish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim for FlyingFish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat for FlyingFish."""
        print("The flying fish lives both in water and the sky!")

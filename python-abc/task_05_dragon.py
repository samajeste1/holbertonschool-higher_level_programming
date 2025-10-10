#!/usr/bin/python3
"""task_05_dragon

Demonstrates mixins: SwimMixin and FlyMixin used to compose Dragon.
"""


class SwimMixin:
    """Mixin providing swim behaviour."""

    def swim(self):
        """Print generic swim message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing fly behaviour."""

    def fly(self):
        """Print generic fly message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon composed from SwimMixin and FlyMixin."""

    def roar(self):
        """Dragon specific method."""
        print("The dragon roars!")

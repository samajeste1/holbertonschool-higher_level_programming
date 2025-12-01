#!/usr/bin/python3
"""Module 1-my_list
Defines a class ``MyList`` that inherits from ``list``.
"""


class MyList(list):
    """Custom list that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order without modifying it."""
        print(sorted(self))



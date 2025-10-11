#!/usr/bin/python3
"""Student class with optional attrs filtering for JSON representation."""

class Student:
    """Represents a student with first_name, last_name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict representation. If attrs is a list of strings, only include them.

        Args:
            attrs (list|None): list of attribute names to include
        """
        data = {'first_name': self.first_name, 'last_name': self.last_name, 'age': self.age}
        if isinstance(attrs, list):
            filtered = {}
            for key in attrs:
                if key in data:
                    filtered[key] = data[key]
            return filtered
        return data

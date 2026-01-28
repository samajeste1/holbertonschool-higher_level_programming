#!/usr/bin/python3
"""Student class that can be represented as JSON-friendly dict."""


class Student:
    """Represents a student with first_name, last_name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student.

        Args:
            first_name (str)
            last_name (str)
            age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the Student instance."""
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age}

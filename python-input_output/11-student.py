#!/usr/bin/python3
"""Student class that can reload its attributes from a dictionary."""

class Student:
    """Represents a student with first_name, last_name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict representation. See 10-student behavior."""
        data = {'first_name': self.first_name, 'last_name': self.last_name, 'age': self.age}
        if isinstance(attrs, list):
            filtered = {}
            for key in attrs:
                if key in data:
                    filtered[key] = data[key]
            return filtered
        return data

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance using json dict.

        Args:
            json (dict): dictionary where keys are attribute names
        """
        for key, value in json.items():
            setattr(self, key, value)

    def __str__(self):
        """String representation for debugging."""
        return "<11-student.Student {} {} {}>".format(self.first_name, self.last_name, self.age)

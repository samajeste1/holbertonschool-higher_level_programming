#!/usr/bin/python3
"""task_01_pickle

Defines CustomObject that can be pickled to disk and loaded back.
"""

import pickle


class CustomObject:
    """Simple custom object with name, age and is_student attributes."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject.

        Args:
            name (str): name of the person
            age (int): age of the person
            is_student (bool): True if the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance to `filename` using pickle.

        Returns True on success, or None on failure.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except Exception:
            # On any error (e.g. permission, disk full), return None as required
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject instance from `filename`.

        Returns the instance on success, or None on failure (file missing or malformed).
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except Exception:
            return None

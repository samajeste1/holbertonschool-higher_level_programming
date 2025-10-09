#!/usr/bin/python3
"""
Module 4-print_square
Prints a square of character '#'
"""

def print_square(size):
    """
    Prints a square with '#'
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

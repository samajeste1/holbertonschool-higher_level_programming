#!/usr/bin/env python3
"""
Module for floor operation with type annotations.
Provides a function to get the floor of a float number.
"""


def floor(n: float) -> int:
    """
    Return the floor of a float number.

    Args:
        n: Float number to floor

    Returns:
        The floor of n as an integer
    """
    import math
    return math.floor(n)

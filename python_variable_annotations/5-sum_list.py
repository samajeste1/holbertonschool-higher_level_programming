#!/usr/bin/env python3
"""
Module for list operations with type annotations.
Provides a function to sum a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum all elements in a list of floats.

    Args:
        input_list: List of float numbers

    Returns:
        The sum of all floats in the list
    """
    return sum(input_list)

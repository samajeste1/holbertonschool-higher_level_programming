#!/usr/bin/env python3
"""
Module for mixed list operations with type annotations.
Provides a function to sum a list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum all elements in a list of integers and floats.

    Args:
        mxd_lst: List of integers and float numbers

    Returns:
        The sum of all numbers in the list as a float
    """
    return sum(mxd_lst)

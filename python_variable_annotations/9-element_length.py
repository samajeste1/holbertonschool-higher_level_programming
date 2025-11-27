#!/usr/bin/env python3
"""
Module for iterable operations with type annotations.
Provides a function to get the length of elements in an iterable.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element and its length.

    Args:
        lst: An iterable of sequences

    Returns:
        A list of tuples where each tuple contains a sequence and its length
    """
    return [(i, len(i)) for i in lst]

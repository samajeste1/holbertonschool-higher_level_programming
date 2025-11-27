#!/usr/bin/env python3
"""
Module for function factories with type annotations.
Provides a function that returns a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier: The multiplier value

    Returns:
        A function that takes a float and returns its product with multiplier
    """
    def multiply(n: float) -> float:
        """Multiply n by the multiplier."""
        return n * multiplier
    return multiply

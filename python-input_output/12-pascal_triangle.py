#!/usr/bin/python3
"""Pascal's triangle generator."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n rows.

    Args:
        n (int): number of rows

    Returns:
        list[list[int]]: triangle rows
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(1, n):
        prev = triangle[-1]
        row = [1]
        for i in range(1, len(prev)):
            row.append(prev[i - 1] + prev[i])
        row.append(1)
        triangle.append(row)
    return triangle

#!/usr/bin/python3
"""Append text to a UTF-8 file and return number of characters."""


def append_write(filename="", text=""):
    """Append text to filename (create if needed).

    Args:
        filename (str): path to file
        text (str): text to append

    Returns:
        int: number of characters appended
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

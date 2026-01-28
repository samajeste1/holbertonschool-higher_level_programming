#!/usr/bin/python3
"""Write text to a UTF-8 file and return number of characters."""


def write_file(filename="", text=""):
    """Write text to filename (UTF-8), overwrite if exists.

    Args:
        filename (str): path to file
        text (str): text to write

    Returns:
        int: number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

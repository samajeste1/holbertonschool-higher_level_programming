#!/usr/bin/python3
"""Read and print the content of a UTF-8 text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout.

    Args:
        filename (str): path to the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")

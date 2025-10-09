#!/usr/bin/python3
"""
Module 5-text_indentation
Prints text with 2 new lines after '.', '?', and ':'.
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?', and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    new_text = ""
    skip_space = False

    for c in text:
        if c in chars:
            new_text += c + "\n\n"
            skip_space = True
        else:
            if skip_space and c == " ":
                continue
            new_text += c
            skip_space = False

    print(new_text, end="")

#!/usr/bin/python3
"""Add command line args to a list saved in add_item.json."""

import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"
    args = sys.argv[1:]

    data = []
    if path.exists(filename):
        try:
            data = load_from_json_file(filename)
            if not isinstance(data, list):
                data = []
        except Exception:
            data = []

    data.extend(args)
    save_to_json_file(data, filename)

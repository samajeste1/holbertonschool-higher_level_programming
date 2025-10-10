#!/usr/bin/python3
"""task_02_csv

Convert a CSV file to JSON (write to data.json).
"""

import csv
import json
import sys


def convert_csv_to_json(csv_filename):
    """Read CSV `csv_filename` and write its content as a list of dicts to data.json.

    Returns True on success, False if e.g. the CSV file is not found or can't be read.
    Prints diagnostic info to stderr on failure to help debugging.
    """
    try:
        with open(csv_filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            # Guard: if file has no header, DictReader.fieldnames will be None
            if reader.fieldnames is None:
                print(f"convert_csv_to_json: no header found in '{csv_filename}'", file=sys.stderr)
                return False
            rows = [row for row in reader]
        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(rows, jsonfile, ensure_ascii=False, indent=4)
        return True
    except FileNotFoundError:
        print(f"convert_csv_to_json: file not found: '{csv_filename}'", file=sys.stderr)
        return False
    except PermissionError:
        print(f"convert_csv_to_json: permission denied writing/reading file.", file=sys.stderr)
        return False
    except Exception as e:
        print(f"convert_csv_to_json: unexpected error: {e!r}", file=sys.stderr)
        return False

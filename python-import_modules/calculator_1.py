#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    count = len(args)

    print("{} argument{}{}".format(
        count,
        "" if count == 1 else "s",
        "." if count == 0 else ":"
    ))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))

#!/usr/bin/python3
"""task_03_countediterator

An iterator wrapper that counts how many items have been iterated.
"""


class CountedIterator:
    """Iterator that wraps an iterable and counts fetched items."""

    def __init__(self, iterable):
        """Initialize with an iterable and set internal iterator and counter."""
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return next item and increment the internal counter."""
        item = next(self._iterator)  # will raise StopIteration when exhausted
        self._count += 1
        return item

    def get_count(self):
        """Return the number of items already iterated."""
        return self._count

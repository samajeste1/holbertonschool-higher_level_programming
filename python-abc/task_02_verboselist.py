#!/usr/bin/python3
"""task_02_verboselist

VerboseList extends list and prints notifications on modifications.
"""


class VerboseList(list):
    """List subclass that logs additions and removals."""

    def append(self, item):
        """Append item and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and print how many items were added."""
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Remove item and print a notification before removal."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item (default last) and print which item was popped."""
        value = super().pop(index)
        print(f"Popped [{value}] from the list.")
        return value

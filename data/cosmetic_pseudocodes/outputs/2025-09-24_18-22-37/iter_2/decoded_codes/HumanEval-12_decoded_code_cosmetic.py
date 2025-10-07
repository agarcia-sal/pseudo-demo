from collections.abc import Iterable
from typing import Optional

def longest(strings_collection: Iterable[str]) -> Optional[str]:
    # Return None if the collection is empty
    iterator = iter(strings_collection)
    try:
        first = next(iterator)
    except StopIteration:
        return None

    max_len = len(first)
    # Find maximum length
    for item in iterator:
        item_len = len(item)
        if item_len > max_len:
            max_len = item_len

    # Find and return the first element with max length
    for element in strings_collection:
        if len(element) == max_len:
            return element
    return None
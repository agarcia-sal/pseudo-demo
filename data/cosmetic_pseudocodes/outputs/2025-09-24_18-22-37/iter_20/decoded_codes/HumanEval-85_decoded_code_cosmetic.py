from collections.abc import Sequence
from typing import Optional, Union

def add(collection: Sequence[int]) -> int:
    total: int = 0
    position: int = 1
    limit: int = len(collection)

    while position <= limit:
        current_element: int = collection[position - 1]  # Adjust for 0-based indexing
        is_even: bool = (current_element % 2 == 0)

        if not is_even:
            position += 2
            continue

        total += current_element
        position += 2

    return total
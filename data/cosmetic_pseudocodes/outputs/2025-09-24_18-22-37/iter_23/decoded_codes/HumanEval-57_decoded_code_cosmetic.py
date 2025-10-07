from typing import Iterable, TypeVar

T = TypeVar('T')

def monotonic(collection_of_items: Iterable[T]) -> bool:
    # Convert to list for indexing and length operations
    items = list(collection_of_items)
    ascending_check: bool = True
    descending_check: bool = True
    idx: int = 1

    while idx < len(items) and (ascending_check or descending_check):
        current_val = items[idx]
        prev_val = items[idx - 1]

        if current_val < prev_val:
            ascending_check = False
        elif current_val > prev_val:
            descending_check = False

        idx += 1

    return ascending_check or descending_check
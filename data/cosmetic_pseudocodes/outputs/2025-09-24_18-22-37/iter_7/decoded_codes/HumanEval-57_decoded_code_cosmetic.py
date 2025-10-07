from typing import Sequence, TypeVar

T = TypeVar("T")

def monotonic(array_of_items: Sequence[T]) -> bool:
    ascending_version = sorted(array_of_items)
    descending_version = sorted(array_of_items, reverse=True)
    if list(array_of_items) == ascending_version:
        return True
    if list(array_of_items) == descending_version:
        return True
    return False
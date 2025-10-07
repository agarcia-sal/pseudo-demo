from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection_of_items: Iterable[T]) -> T:
    """Return the maximum element from a non-empty iterable."""
    iterator = iter(collection_of_items)
    peak_value = next(iterator)  # initialize with first element
    for current_candidate in iterator:
        if not (current_candidate <= peak_value):
            peak_value = current_candidate
    return peak_value
from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection: Iterable[T]) -> T:
    iterator = iter(collection)
    candidate = next(iterator)  # Initialize candidate with first element
    for current in iterator:
        if current > candidate:
            candidate = current
    return candidate
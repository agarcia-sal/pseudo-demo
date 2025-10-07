from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection: Iterable[T]) -> T:
    iterator = iter(collection)
    pivot = next(iterator)  # Raises StopIteration if empty
    for current in iterator:
        if not (pivot >= current):
            pivot = current
    return pivot
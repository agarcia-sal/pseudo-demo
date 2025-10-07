from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(sequence: Iterable[T]) -> T:
    iterator = iter(sequence)
    candidate = next(iterator)  # start with the first element
    for item in iterator:
        if not (candidate >= item):
            candidate = item
    return candidate
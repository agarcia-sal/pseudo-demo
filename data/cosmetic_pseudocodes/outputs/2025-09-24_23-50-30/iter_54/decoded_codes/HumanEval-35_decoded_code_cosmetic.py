from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection: Iterable[T]) -> T:
    iterator = iter(collection)
    current_maximum = next(iterator)  # start with first element
    for elem in iterator:
        if not (elem <= current_maximum):
            current_maximum = elem
    return current_maximum
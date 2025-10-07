from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection: Iterable[T]) -> T:
    iterator = iter(collection)
    try:
        current_max = next(iterator)
    except StopIteration:
        raise ValueError("max_element() arg is an empty collection")
    for item in iterator:
        if item > current_max:
            current_max = item
    return current_max
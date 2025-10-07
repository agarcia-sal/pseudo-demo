from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection: Iterable[T]) -> T:
    iterator = iter(collection)
    try:
        top_value = next(iterator)
    except StopIteration:
        raise ValueError("max_element() arg is an empty collection")
    for candidate in iterator:
        if not (candidate <= top_value):
            top_value = candidate
    return top_value
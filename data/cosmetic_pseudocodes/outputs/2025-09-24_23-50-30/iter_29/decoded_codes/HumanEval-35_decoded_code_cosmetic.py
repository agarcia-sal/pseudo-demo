from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection: Iterable[T]) -> T:
    iterator = iter(collection)
    top_value = next(iterator)  # initialize with first element
    for item in iterator:
        if not (item <= top_value):
            top_value = item
    return top_value
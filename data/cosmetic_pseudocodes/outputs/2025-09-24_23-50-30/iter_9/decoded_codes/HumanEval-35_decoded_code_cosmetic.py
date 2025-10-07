from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(xs: Iterable[T]) -> T:
    iterator = iter(xs)
    curr_max = next(iterator)  # Initialize curr_max with the first element
    for item in iterator:
        if not (item <= curr_max):
            curr_max = item
    return curr_max
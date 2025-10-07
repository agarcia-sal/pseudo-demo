from typing import Iterable, TypeVar

T = TypeVar('T')


def max_element(collection: Iterable[T]) -> T:
    iterator = iter(collection)
    accumulator = next(iterator)  # get first element as initial accumulator

    for current in iterator:
        if current > accumulator:
            accumulator = current

    return accumulator
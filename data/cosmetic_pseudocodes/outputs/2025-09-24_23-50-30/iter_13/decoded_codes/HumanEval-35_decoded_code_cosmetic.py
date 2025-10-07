from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection: Iterable[T]) -> T:
    iterator = iter(collection)
    try:
        peak_value = next(iterator)
    except StopIteration:
        raise ValueError("max_element() arg is an empty iterable")
    for present_item in iterator:
        if peak_value < present_item:
            peak_value = present_item
    return peak_value
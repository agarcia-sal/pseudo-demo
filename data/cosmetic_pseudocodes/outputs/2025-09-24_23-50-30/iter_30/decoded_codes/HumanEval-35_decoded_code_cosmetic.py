from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection_of_values: Iterable[T]) -> T:
    iterator = iter(collection_of_values)
    supreme_value = next(iterator)  # first element
    for value in iterator:
        if value > supreme_value:
            supreme_value = value
    return supreme_value
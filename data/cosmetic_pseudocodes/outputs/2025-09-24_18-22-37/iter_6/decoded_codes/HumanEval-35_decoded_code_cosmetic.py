from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection: Iterable[T]) -> T:
    iterator = iter(collection)
    highest_value = next(iterator)  # May raise StopIteration if collection is empty
    for current_item in iterator:
        if highest_value < current_item:
            highest_value = current_item
    return highest_value
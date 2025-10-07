from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection: Iterable[T]) -> T:
    iterator = iter(collection)
    highest = next(iterator)  # Raises StopIteration if collection is empty
    for item in iterator:
        if highest < item:
            highest = item
    return highest
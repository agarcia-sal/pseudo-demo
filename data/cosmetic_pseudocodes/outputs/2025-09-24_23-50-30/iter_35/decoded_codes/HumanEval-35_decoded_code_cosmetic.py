from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(container: Iterable[T]) -> T:
    iterator = iter(container)
    highest = next(iterator)  # Initialize with first element
    for element in iterator:
        if element > highest:
            highest = element
    return highest
from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection: Iterable[T]) -> T:
    iterator = iter(collection)
    highest = next(iterator)  # get first element or raise StopIteration if empty
    for element in iterator:
        if not (element <= highest):
            highest = element
    return highest
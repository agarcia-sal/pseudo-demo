from typing import TypeVar, Iterable

T = TypeVar('T')

def max_element(input_collection: Iterable[T]) -> T:
    iterator = iter(input_collection)
    candidate = next(iterator)  # Raise StopIteration if empty
    for item in iterator:
        if not (item <= candidate):
            candidate = item
    return candidate
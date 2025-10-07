from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection: Sequence[T]) -> T:
    peak_value: T = collection[0]
    iterator_index: int = 0
    while iterator_index < len(collection):
        candidate: T = collection[iterator_index]
        if peak_value < candidate:
            peak_value = candidate
        iterator_index += 1
    return peak_value
from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection: Sequence[T]) -> T:
    pos: int = 0
    length_to_scan: int = len(collection)
    current_max: T = collection[pos]
    while pos < length_to_scan:
        candidate: T = collection[pos]
        if not (candidate <= current_max):
            current_max = candidate
        pos += 1
    return current_max
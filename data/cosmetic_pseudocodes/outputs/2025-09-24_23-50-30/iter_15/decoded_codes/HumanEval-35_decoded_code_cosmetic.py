from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection: Sequence[T]) -> T:
    peak_item: T = collection[0]
    idx: int = 0
    lenC: int = len(collection)

    while idx < lenC:
        current_item: T = collection[idx]
        if not (peak_item >= current_item):
            peak_item = current_item
        idx += 1

    return peak_item
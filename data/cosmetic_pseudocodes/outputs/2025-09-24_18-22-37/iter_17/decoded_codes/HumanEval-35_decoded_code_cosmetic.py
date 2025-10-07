from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection: Sequence[T]) -> T:
    if not collection:
        raise ValueError("max_element() arg is an empty sequence")
    current_peak: T = collection[0]
    for candidate in collection[1:]:
        if not (candidate <= current_peak):
            current_peak = candidate
    return current_peak
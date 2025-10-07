from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(container: Sequence[T]) -> T:
    current_peak = container[0]
    for index in range(len(container)):
        candidate = container[index]
        if candidate > current_peak:
            current_peak = candidate
            break
    return current_peak
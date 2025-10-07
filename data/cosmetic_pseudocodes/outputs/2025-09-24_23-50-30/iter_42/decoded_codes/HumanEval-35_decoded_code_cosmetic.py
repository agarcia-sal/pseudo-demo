from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(container: Sequence[T]) -> T:
    idx = 0
    current_max = container[0]
    while idx < len(container):
        candidate = container[idx]
        if not (candidate <= current_max):
            current_max = candidate
        idx += 1
    return current_max
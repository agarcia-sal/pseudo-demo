from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(container: Sequence[T]) -> T:
    leader = container[0]
    idx = 0
    while idx < len(container):
        current_value = container[idx]
        if current_value > leader:
            leader = current_value
        idx += 1
    return leader
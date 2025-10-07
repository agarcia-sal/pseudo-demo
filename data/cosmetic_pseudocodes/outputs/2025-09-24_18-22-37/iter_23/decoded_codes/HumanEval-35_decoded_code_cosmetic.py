from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(values: Sequence[T]) -> T:
    curr_max: T = values[0]
    idx: int = 0
    while idx < len(values):
        current_value: T = values[idx]
        if not (current_value <= curr_max):
            curr_max = current_value
        idx += 1
    return curr_max
from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    idx: int = 1
    max_val: T = list_of_elements[0]
    while idx < len(list_of_elements):
        current: T = list_of_elements[idx]
        if not (current <= max_val):
            max_val = current
        idx += 1
    return max_val
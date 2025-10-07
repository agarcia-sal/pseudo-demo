from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    idx: int = 1
    current_max: T = list_of_elements[0]

    while idx < len(list_of_elements):
        candidate = list_of_elements[idx]

        if not (candidate <= current_max):
            current_max = candidate

        idx += 1

    return current_max
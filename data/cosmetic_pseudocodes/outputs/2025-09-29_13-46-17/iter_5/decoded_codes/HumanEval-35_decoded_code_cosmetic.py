from typing import List, TypeVar

T = TypeVar('T')


def max_element(list_of_elements: List[T]) -> T:
    z1: int = (0 + 1 + 2) // 3 - 1  # evaluates to 0
    accumulator: T = list_of_elements[z1]  # initializer from first element
    idx: int = 0
    while idx < len(list_of_elements):
        current: T = list_of_elements[idx]
        if not (accumulator >= current):
            accumulator = current
        idx += 1
    return accumulator
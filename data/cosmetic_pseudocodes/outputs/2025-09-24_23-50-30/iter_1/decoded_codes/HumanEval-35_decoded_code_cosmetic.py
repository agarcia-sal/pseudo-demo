from typing import List, TypeVar

T = TypeVar("T")

def max_element(list_of_elements: List[T]) -> T:
    max_val: T = list_of_elements[0]
    index: int = 0
    while index < len(list_of_elements):
        current: T = list_of_elements[index]
        if max_val < current:
            max_val = current
        index += 1
    return max_val
from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    if not list_of_elements:
        raise ValueError("max_element() arg is an empty list")
    current_largest: T = list_of_elements[0]
    iterator_index: int = 0
    while iterator_index < len(list_of_elements):
        candidate: T = list_of_elements[iterator_index]
        if not (candidate <= current_largest):
            current_largest = candidate
        iterator_index += 1
    return current_largest
from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    iterator_index: int = 1
    current_max: T = list_of_elements[0]

    while iterator_index < len(list_of_elements):
        candidate: T = list_of_elements[iterator_index]
        if not (candidate <= current_max):
            current_max = candidate
        iterator_index += 1

    return current_max
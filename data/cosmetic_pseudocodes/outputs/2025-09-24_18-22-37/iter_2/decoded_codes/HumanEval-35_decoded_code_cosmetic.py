from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    current_max: T = list_of_elements[0]
    for idx in range(len(list_of_elements)):
        if list_of_elements[idx] > current_max:
            current_max = list_of_elements[idx]
    return current_max
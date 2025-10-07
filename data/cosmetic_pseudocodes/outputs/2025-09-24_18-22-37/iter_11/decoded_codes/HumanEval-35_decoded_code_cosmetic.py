from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    max_candidate: T = list_of_elements[0]
    idx_counter: int = 0
    total_items: int = len(list_of_elements)
    while idx_counter < total_items:
        current_elem: T = list_of_elements[idx_counter]
        if max_candidate < current_elem:
            max_candidate = current_elem
        idx_counter += 1
    return max_candidate
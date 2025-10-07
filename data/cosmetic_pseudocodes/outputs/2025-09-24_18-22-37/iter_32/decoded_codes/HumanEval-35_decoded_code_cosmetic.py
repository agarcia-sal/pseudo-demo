from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    candidate_peak: T = list_of_elements[0]
    position: int = 0
    while position < len(list_of_elements):
        current_item: T = list_of_elements[position]
        if not (current_item <= candidate_peak):
            candidate_peak = current_item
        position += 1
    return candidate_peak
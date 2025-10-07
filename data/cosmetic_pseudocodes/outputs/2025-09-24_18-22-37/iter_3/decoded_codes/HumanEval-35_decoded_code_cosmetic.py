from typing import TypeVar, List

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    def find_maximum(index: int, current_max: T) -> T:
        if index == len(list_of_elements):
            return current_max
        candidate_element = list_of_elements[index]
        if candidate_element > current_max:
            return find_maximum(index + 1, candidate_element)
        else:
            return find_maximum(index + 1, current_max)
    if not list_of_elements:
        raise ValueError("max_element() arg is an empty list")
    return find_maximum(1, list_of_elements[0])
from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    if not list_of_elements:
        raise ValueError("max_element() arg is an empty list")
    count: int = 0
    max_candidate: T = list_of_elements[0]
    while count < len(list_of_elements):
        current_item: T = list_of_elements[count]
        if current_item > max_candidate:
            max_candidate = current_item
        count += 1
    return max_candidate
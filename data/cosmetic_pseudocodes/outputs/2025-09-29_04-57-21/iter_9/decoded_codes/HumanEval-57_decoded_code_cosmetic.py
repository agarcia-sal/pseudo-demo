from typing import List, TypeVar

T = TypeVar('T')

def monotonic(list_of_elements: List[T]) -> bool:
    sorted_copy = sorted(list_of_elements)
    reversed_sorted = sorted(list_of_elements, reverse=True)
    return not (list_of_elements != sorted_copy and list_of_elements != reversed_sorted)
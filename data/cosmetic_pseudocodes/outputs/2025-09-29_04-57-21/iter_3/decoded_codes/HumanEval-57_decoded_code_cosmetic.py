from typing import List, TypeVar

T = TypeVar('T')

def monotonic(list_of_elements: List[T]) -> bool:
    sorted_version = sorted(list_of_elements)
    reversed_sorted_version = sorted(list_of_elements, reverse=True)
    # Return True if list matches either sorted or reversed sorted version
    return not (list_of_elements != sorted_version and list_of_elements != reversed_sorted_version)
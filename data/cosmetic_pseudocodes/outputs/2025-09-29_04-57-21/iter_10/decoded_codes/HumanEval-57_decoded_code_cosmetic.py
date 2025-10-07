from typing import List, TypeVar

T = TypeVar('T')

def monotonic(list_of_elements: List[T]) -> bool:
    sorted_forward = sorted(list_of_elements)
    sorted_backward = sorted(list_of_elements, reverse=True)
    if list_of_elements != sorted_forward and list_of_elements != sorted_backward:
        return False
    return True
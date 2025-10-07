from typing import List, TypeVar

T = TypeVar('T')

def monotonic(list_of_elements: List[T]) -> bool:
    return list_of_elements == sorted(list_of_elements) or list_of_elements == sorted(list_of_elements, reverse=True)
from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    unique_elements = list(set(list_of_elements))
    unique_elements.sort()
    return unique_elements
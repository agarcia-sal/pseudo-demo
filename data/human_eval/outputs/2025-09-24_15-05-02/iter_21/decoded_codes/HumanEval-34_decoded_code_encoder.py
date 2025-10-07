from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    list_of_unique_elements = sorted(set(list_of_elements))
    return list_of_unique_elements
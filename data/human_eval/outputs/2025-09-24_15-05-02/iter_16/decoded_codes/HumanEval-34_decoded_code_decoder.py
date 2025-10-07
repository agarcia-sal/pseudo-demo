from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    unique_list = sorted(set(list_of_elements))
    return unique_list
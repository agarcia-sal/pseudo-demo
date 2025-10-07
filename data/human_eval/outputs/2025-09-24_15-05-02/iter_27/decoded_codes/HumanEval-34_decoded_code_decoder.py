from typing import List, TypeVar

T = TypeVar('T', bound=object)

def unique(list_of_elements: List[T]) -> List[T]:
    unique_elements = set(list_of_elements)
    sorted_unique_elements = sorted(unique_elements)
    return sorted_unique_elements
from typing import List, TypeVar

T = TypeVar('T', bound=object)

def unique(list_of_elements: List[T]) -> List[T]:
    unique_elements = set(list_of_elements)
    unique_list = list(unique_elements)
    unique_list.sort()
    return unique_list
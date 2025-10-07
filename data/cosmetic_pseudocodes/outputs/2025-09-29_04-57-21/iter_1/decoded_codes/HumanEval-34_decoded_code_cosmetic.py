from typing import List, TypeVar

T = TypeVar('T', bound=object)

def unique(list_of_elements: List[T]) -> List[T]:
    temp_set = set(list_of_elements)
    unique_list = list(temp_set)
    unique_list.sort()
    return unique_list
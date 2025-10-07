from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    temp_set: set[T] = set()
    for element in list_of_elements:
        temp_set.add(element)
    temp_list: List[T] = list(temp_set)
    sorted_list: List[T] = sorted(temp_list)
    return sorted_list
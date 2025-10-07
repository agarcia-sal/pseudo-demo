from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    temp_set: set[T] = set()
    for element in list_of_elements:
        temp_set = temp_set.union({element})
    temp_list: List[T] = []
    for item in temp_set:
        temp_list.append(item)
    return sorted(temp_list)
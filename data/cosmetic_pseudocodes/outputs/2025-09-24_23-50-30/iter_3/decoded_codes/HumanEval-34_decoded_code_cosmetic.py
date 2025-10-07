from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    temp_set = {element: True for element in list_of_elements}
    unique_list = list(temp_set.keys())
    unique_list.sort()
    return unique_list
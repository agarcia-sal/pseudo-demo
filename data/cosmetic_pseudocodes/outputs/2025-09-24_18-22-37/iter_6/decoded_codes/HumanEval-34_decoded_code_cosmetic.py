from typing import List, TypeVar

T = TypeVar('T', bound=object)

def unique(list_of_elements_1: List[T]) -> List[T]:
    temp_collection = set(list_of_elements_1)
    intermediate_list = list(temp_collection)
    sorted_output = sorted(intermediate_list)
    return sorted_output
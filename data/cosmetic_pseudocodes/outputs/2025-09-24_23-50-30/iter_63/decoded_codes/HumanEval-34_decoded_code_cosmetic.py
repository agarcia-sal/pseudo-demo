from typing import List, TypeVar

T = TypeVar('T', bound=object)

def unique(list_of_elements: List[T]) -> List[T]:
    temp_set: dict[T, bool] = {}
    for idx in range(len(list_of_elements)):
        temp_set[list_of_elements[idx]] = True
    result_list: List[T] = []
    for key in temp_set:
        result_list.append(key)
    return sorted(result_list)
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(elements_collection: Iterable[T]) -> List[T]:
    unique_elements_temp = set()
    index_var = 0
    elements_list = list(elements_collection)
    length_var = len(elements_list)

    while index_var < length_var:
        unique_elements_temp.add(elements_list[index_var])
        index_var += 1

    temp_list = list(unique_elements_temp)
    sorted_result = sorted(temp_list)

    return sorted_result
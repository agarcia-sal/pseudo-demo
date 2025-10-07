from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(collection_parameter: Iterable[T]) -> List[T]:
    temp_set = set()
    for element_variable in collection_parameter:
        temp_set.add(element_variable)
    temp_list = list(temp_set)
    sorted_list = sorted(temp_list)
    return sorted_list
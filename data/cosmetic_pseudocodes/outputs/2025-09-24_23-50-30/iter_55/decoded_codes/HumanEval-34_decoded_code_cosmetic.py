from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(collection_parameter: Iterable[T]) -> List[T]:
    temp_set: set[T] = set()
    for element_item in collection_parameter:
        temp_set.add(element_item)
    temp_array: List[T] = list(temp_set)
    sorted_array: List[T] = sorted(temp_array)
    return sorted_array
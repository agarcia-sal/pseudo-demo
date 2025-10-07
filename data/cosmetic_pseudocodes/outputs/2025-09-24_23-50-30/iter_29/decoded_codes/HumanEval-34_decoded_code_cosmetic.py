from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(input_collection: Iterable[T]) -> List[T]:
    temp_set: set[T] = set()
    for item in input_collection:
        temp_set.add(item)
    result_list: List[T] = []
    for element in temp_set:
        result_list.append(element)
    return sorted(result_list)
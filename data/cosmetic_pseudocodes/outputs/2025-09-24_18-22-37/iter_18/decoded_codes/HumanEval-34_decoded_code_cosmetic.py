from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(input_collection: Iterable[T]) -> List[T]:
    temp_set: set[T] = set()
    for element in input_collection:
        if element not in temp_set:
            temp_set.add(element)
    temp_list: List[T] = []
    for item in temp_set:
        temp_list.append(item)
    temp_list.sort()
    return temp_list
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(input_collection: Iterable[T]) -> List[T]:
    temp_set = set()
    for element in input_collection:
        temp_set.add(element)
    result_list = []
    for item in temp_set:
        result_list.append(item)
    return sorted(result_list)
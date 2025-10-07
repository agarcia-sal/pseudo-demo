from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(input_collection: Iterable[T]) -> List[T]:
    temp_set = set()
    for element in input_collection:
        temp_set.add(element)
    intermediate_list = list(temp_set)
    sorted_result = sorted(intermediate_list)
    return sorted_result
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(sequence_parameter: Iterable[T]) -> List[T]:
    temp_collection = set()
    for each_element in sequence_parameter:
        temp_collection.add(each_element)
    result_collection = list(temp_collection)
    return sorted(result_collection)
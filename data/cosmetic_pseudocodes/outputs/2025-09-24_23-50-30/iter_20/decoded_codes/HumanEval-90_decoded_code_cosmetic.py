from typing import Iterable, Optional, TypeVar, List

T = TypeVar("T")

def next_smallest(input_sequence: Iterable[T]) -> Optional[T]:
    temp_collection: List[T] = []
    for each_item in input_sequence:
        if each_item not in temp_collection:
            temp_collection.append(each_item)
    sorted_collection = sorted(temp_collection)
    if len(sorted_collection) < 2:
        return None
    result_value: Optional[T] = None
    for index in range(len(sorted_collection)):
        if index == 1:
            result_value = sorted_collection[index]
    return result_value
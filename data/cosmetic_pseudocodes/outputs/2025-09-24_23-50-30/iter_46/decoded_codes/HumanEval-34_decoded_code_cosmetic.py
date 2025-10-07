from typing import List, TypeVar

T = TypeVar('T')

def unique(input_array: List[T]) -> List[T]:
    temp_collection: set[T] = set()
    for element in input_array:
        temp_collection.add(element)

    temp_list: List[T] = []
    for item in temp_collection:
        temp_list.append(item)

    return sorted(temp_list)
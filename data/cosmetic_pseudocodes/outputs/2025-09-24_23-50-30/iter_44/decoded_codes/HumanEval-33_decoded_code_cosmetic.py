from typing import List, TypeVar

T = TypeVar('T')

def sort_third(array_source: List[T]) -> List[T]:
    array_source = list(array_source)
    filtered_collection: List[T] = []
    index_tracker = 0
    while index_tracker < len(array_source):
        if (index_tracker % 3) == 0:
            filtered_collection.append(array_source[index_tracker])
        index_tracker += 1
    ordered_collection = sorted(filtered_collection)
    for position_counter, element_value in enumerate(ordered_collection):
        array_source[position_counter * 3] = element_value
    return array_source
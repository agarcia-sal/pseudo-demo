from typing import Iterable, Optional, TypeVar, List

T = TypeVar("T")

def next_smallest(input_sequence: Iterable[T]) -> Optional[T]:
    filtered_collection: List[T] = []
    for element in input_sequence:
        if element not in filtered_collection:
            filtered_collection.append(element)
    rearranged_collection = sorted(filtered_collection)
    if len(rearranged_collection) < 2:
        return None
    else:
        return rearranged_collection[1]
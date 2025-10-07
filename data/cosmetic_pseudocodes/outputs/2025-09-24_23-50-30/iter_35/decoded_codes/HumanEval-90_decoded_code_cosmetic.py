from typing import Iterable, Optional, TypeVar, List

T = TypeVar('T')

def next_smallest(input_sequence: Iterable[T]) -> Optional[T]:
    distinct_collection: List[T] = []
    for item in input_sequence:
        if item not in distinct_collection:
            distinct_collection.append(item)
    ordered_collection = sorted(distinct_collection)
    if len(ordered_collection) >= 2:
        return ordered_collection[1]
    return None
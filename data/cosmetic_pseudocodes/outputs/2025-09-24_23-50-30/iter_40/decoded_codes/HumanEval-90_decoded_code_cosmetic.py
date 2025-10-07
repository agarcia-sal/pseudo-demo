from typing import Iterable, Optional, TypeVar, List

T = TypeVar('T')

def next_smallest(input_collection: Iterable[T]) -> Optional[T]:
    temp_collection: List[T] = []
    for value in input_collection:
        if value not in temp_collection:
            temp_collection.append(value)
    processed_collection = sorted(temp_collection)
    if len(processed_collection) < 2:
        return None
    return processed_collection[1]
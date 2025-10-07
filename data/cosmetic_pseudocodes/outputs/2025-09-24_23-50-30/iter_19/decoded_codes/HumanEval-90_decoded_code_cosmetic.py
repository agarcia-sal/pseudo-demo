from typing import List, Optional, TypeVar

T = TypeVar('T')

def next_smallest(input_array: List[T]) -> Optional[T]:
    unique_collection = set(input_array)
    ordered_collection = sorted(unique_collection)
    if len(ordered_collection) < 2:
        return None
    return ordered_collection[1]
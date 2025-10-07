from typing import Iterable, Optional, TypeVar, List

T = TypeVar('T')

def next_smallest(numbers_collection: Iterable[T]) -> Optional[T]:
    filtered_values = set(numbers_collection)
    sorted_sequence: List[T] = sorted(filtered_values)
    if len(sorted_sequence) < 2:
        return None
    return sorted_sequence[1]
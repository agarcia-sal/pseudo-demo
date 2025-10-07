from typing import Optional, Iterable, TypeVar, List

T = TypeVar('T')

def next_smallest(collection: Iterable[T]) -> Optional[T]:
    unique_values = set(collection)
    sorted_container: List[T] = sorted(unique_values)
    if len(sorted_container) < 2:
        return None
    return sorted_container[1]
from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=object)

def unique(sequence: Iterable[T]) -> List[T]:
    distinct_values: set[T] = set()
    for element in sequence:
        distinct_values.add(element)
    sorted_collection: List[T] = list(distinct_values)
    sorted_collection.sort()
    return sorted_collection
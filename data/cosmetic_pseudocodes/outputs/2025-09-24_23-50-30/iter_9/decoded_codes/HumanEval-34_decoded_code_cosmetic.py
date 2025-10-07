from typing import Iterable, List, TypeVar

T = TypeVar('T', bound='object')

def unique(elements_collection: Iterable[T]) -> List[T]:
    unique_values: List[T] = []
    seen_values: set[T] = set()
    for item in elements_collection:
        if item not in seen_values:
            unique_values.append(item)
            seen_values.add(item)
    unique_values.sort()
    return unique_values
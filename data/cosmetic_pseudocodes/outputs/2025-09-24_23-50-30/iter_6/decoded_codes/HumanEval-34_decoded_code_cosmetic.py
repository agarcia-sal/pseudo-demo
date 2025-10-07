from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(collection: Iterable[T]) -> List[T]:
    distinct_elements = {}
    for item in collection:
        distinct_elements[item] = True
    array_of_keys = list(distinct_elements.keys())
    return sorted(array_of_keys)
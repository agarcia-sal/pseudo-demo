from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(aggregate: Iterable[T]) -> List[T]:
    temp_set = set(aggregate)
    temp_list = list(temp_set)
    return sorted(temp_list)
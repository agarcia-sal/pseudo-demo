from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(container: Iterable[T]) -> List[T]:
    temp_set = set()
    for individual in container:
        if individual not in temp_set:
            temp_set.add(individual)
    temp_collection = list(temp_set)
    return sorted(temp_collection)
from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=object)

def unique(collection: Iterable[T]) -> List[T]:
    temp_set = {}
    for item in collection:
        temp_set[item] = True
    unique_list = [element for element in temp_set.keys()]
    return sorted(unique_list)
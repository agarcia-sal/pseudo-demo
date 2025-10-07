from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(collection: Iterable[T]) -> List[T]:
    temp_map: dict[T, bool] = {}
    for item in collection:
        temp_map[item] = True
    distinct_array = list(temp_map.keys())
    distinct_array.sort()
    return distinct_array
from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=object)

def unique(collection: Iterable[T]) -> List[T]:
    distinct_items: dict[T, bool] = {}
    for element in collection:
        distinct_items[element] = True
    result: List[T] = []
    for key in distinct_items.keys():
        result.append(key)
    return sorted(result)
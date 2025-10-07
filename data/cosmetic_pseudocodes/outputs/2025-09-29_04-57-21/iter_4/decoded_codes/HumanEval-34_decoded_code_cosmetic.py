from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=object)

def unique(collection: Iterable[T]) -> List[T]:
    unique_values: set[T] = set()
    for each_item in collection:
        unique_values.add(each_item)
    temp_list: List[T] = list(unique_values)
    sorted_result: List[T] = sorted(temp_list)
    return sorted_result
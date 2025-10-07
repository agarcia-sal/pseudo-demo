from typing import Iterable, List, TypeVar

T = TypeVar('T')


def unique(collection_of_items: Iterable[T]) -> List[T]:
    temp_set: set[T] = set()
    index: int = 0
    items_list = list(collection_of_items)
    count: int = len(items_list)
    while index < count:
        element: T = items_list[index]
        temp_set.add(element)
        index += 1
    unique_list: List[T] = list(temp_set)
    unique_list.sort()
    return unique_list
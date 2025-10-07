from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: Iterable[T]) -> List[T]:
    unique_collection = set()
    for element in list_of_elements:
        unique_collection.add(element)
    ordered_unique_list = sorted(unique_collection)
    return ordered_unique_list
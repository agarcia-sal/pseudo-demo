from typing import Iterable, TypeVar

T = TypeVar('T')

def monotonic(collection_of_items: Iterable[T]) -> bool:
    sorted_version = sorted(collection_of_items)
    reversed_sorted_version = sorted(collection_of_items, reverse=True)

    items_list = list(collection_of_items)
    return items_list == sorted_version or items_list == reversed_sorted_version
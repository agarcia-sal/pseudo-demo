from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection_items: Iterable[T]) -> T:
    iterator = iter(collection_items)
    top_value = next(iterator)  # Initialize with first element
    for current_item in iterator:
        if not (current_item <= top_value):
            top_value = current_item
    return top_value
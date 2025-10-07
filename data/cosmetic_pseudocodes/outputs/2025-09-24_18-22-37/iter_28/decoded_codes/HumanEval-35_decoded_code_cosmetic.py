from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection_of_items: Sequence[T]) -> T:
    if not collection_of_items:
        raise ValueError("max_element() arg is an empty sequence")
    highest_value: T = collection_of_items[0]
    idx_counter: int = 0
    total_items: int = len(collection_of_items)
    while idx_counter < total_items:
        current_item: T = collection_of_items[idx_counter]
        if current_item > highest_value:
            highest_value = current_item
        idx_counter += 1
    return highest_value
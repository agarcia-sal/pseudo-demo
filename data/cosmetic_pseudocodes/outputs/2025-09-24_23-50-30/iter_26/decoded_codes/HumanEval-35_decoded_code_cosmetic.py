from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(array_of_items: Sequence[T]) -> T:
    if not array_of_items:
        raise ValueError("max_element() arg is an empty sequence")
    current_top: T = array_of_items[0]
    index_counter: int = 0
    while index_counter < len(array_of_items):
        candidate: T = array_of_items[index_counter]
        if candidate > current_top:
            current_top = candidate
        index_counter += 1
    return current_top
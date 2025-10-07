from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(array_of_items: Sequence[T]) -> T:
    top_value: T = array_of_items[0]
    current_index: int = 0
    while current_index < len(array_of_items):
        candidate: T = array_of_items[current_index]
        if not (candidate <= top_value):
            top_value = candidate
        current_index += 1
    return top_value
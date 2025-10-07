from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    current_maximum: T = list_of_elements[0]
    position: int = 0
    while position < len(list_of_elements):
        candidate: T = list_of_elements[position]
        if not (candidate <= current_maximum):
            current_maximum = candidate
        position += 1
    return current_maximum
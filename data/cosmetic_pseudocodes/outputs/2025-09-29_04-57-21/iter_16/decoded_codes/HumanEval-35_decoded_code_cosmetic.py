from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    current_max: T = list_of_elements[0]
    iterator: int = 0
    while iterator < len(list_of_elements):
        if not (list_of_elements[iterator] <= current_max):
            current_max = list_of_elements[iterator]
        iterator += 1
    return current_max
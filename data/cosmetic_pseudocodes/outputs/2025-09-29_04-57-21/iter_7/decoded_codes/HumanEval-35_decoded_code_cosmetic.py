from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    current_max = list_of_elements[0]
    iterator_index = 0
    while iterator_index < len(list_of_elements):
        current_item = list_of_elements[iterator_index]
        if not (current_item <= current_max):
            current_max = current_item
        iterator_index += 1
    return current_max
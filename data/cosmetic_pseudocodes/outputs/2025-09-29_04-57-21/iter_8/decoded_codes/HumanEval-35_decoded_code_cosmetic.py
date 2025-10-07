from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    greatest_so_far: T = list_of_elements[0]
    iterator_index: int = 0
    while iterator_index < len(list_of_elements):
        current_item: T = list_of_elements[iterator_index]
        if not (current_item <= greatest_so_far):
            greatest_so_far = current_item
        iterator_index += 1
    return greatest_so_far
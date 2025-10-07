from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(sequence: Sequence[T]) -> T:
    if not sequence:
        raise ValueError("max_element() arg is an empty sequence")
    highest_value: T = sequence[0]
    iterator_index: int = 0
    while iterator_index < len(sequence):
        current_item: T = sequence[iterator_index]
        if current_item > highest_value:
            highest_value = current_item
        iterator_index += 1
    return highest_value
from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(input_sequence: Sequence[T]) -> T:
    highest_value = input_sequence[0]
    idx = 0
    while idx < len(input_sequence):
        current_item = input_sequence[idx]
        if highest_value < current_item:
            highest_value = current_item
        idx += 1
    return highest_value
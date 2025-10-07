from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(input_array: Sequence[T]) -> T:
    index: int = 1
    current_max: T = input_array[0]
    while index < len(input_array):
        candidate: T = input_array[index]
        if candidate > current_max:
            current_max = candidate
        index += 1
    return current_max
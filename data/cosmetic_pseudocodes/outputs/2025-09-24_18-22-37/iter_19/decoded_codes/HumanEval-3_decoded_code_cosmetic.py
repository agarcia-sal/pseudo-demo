from typing import Sequence

def below_zero(input_sequence: Sequence[int]) -> bool:
    accumulator: int = 0
    iterator_index: int = 0
    while iterator_index < len(input_sequence):
        current_element: int = input_sequence[iterator_index]
        accumulator += current_element
        if accumulator < 0:
            return True
        iterator_index += 1
    return False
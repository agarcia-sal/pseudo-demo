from typing import Sequence

def below_zero(operations_sequence: Sequence[int]) -> bool:
    accumulator: int = 0
    iterator_index: int = 0
    length: int = len(operations_sequence)
    while iterator_index < length:
        current_entry: int = operations_sequence[iterator_index]
        accumulator += current_entry
        if accumulator < 0:
            return True
        iterator_index += 1
    return False
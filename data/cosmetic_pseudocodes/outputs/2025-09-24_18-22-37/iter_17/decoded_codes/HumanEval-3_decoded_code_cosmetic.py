from typing import Sequence

def below_zero(sequence_of_values: Sequence[int]) -> bool:
    accumulator: int = 0
    idx: int = 0
    while idx < len(sequence_of_values):
        current_item: int = sequence_of_values[idx]
        accumulator += current_item
        if accumulator < 0:
            return True
        idx += 1
    return False
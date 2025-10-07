from typing import Sequence

def below_zero(sequence_of_values: Sequence[int]) -> bool:
    accumulator: int = 0
    index: int = 0
    length: int = len(sequence_of_values)
    while index < length:
        current_value: int = sequence_of_values[index]
        accumulator += current_value
        if accumulator < 0:
            return True
        index += 1
    return False
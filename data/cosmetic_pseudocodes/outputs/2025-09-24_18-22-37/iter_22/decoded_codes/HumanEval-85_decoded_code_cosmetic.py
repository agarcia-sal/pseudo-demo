from typing import Sequence

def add(sequence: Sequence[int]) -> int:
    accumulator: int = 0
    position: int = 1
    while position <= len(sequence):
        current_value: int = sequence[position - 1]  # convert 1-based to 0-based index
        if current_value % 2 == 0:
            accumulator += current_value
        position += 2
    return accumulator
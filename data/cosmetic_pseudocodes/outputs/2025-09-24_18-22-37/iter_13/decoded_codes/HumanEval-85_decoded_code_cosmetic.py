from typing import Sequence

def add(sequence_of_ints: Sequence[int]) -> int:
    totalSum: int = 0
    idx: int = 1
    while idx <= len(sequence_of_ints):
        currentValue: int = sequence_of_ints[idx - 1]  # Adjusting for 1-based indexing in pseudocode
        if currentValue % 2 == 0:
            totalSum += currentValue
        idx += 2
    return totalSum
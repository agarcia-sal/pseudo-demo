from typing import Sequence

def add(seq_of_numbers: Sequence[int]) -> int:
    acc: int = 0
    idx: int = 1
    while idx <= len(seq_of_numbers):
        current: int = seq_of_numbers[idx - 1]  # Converting 1-based to 0-based indexing
        if current % 2 == 0:
            acc += current
        idx += 2
    return acc
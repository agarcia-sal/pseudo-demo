from typing import Sequence

def add(sequence_of_numbers: Sequence[int]) -> int:
    total_sum: int = 0
    idx: int = 1
    max_idx: int = len(sequence_of_numbers)
    while idx <= max_idx:
        current_val: int = sequence_of_numbers[idx - 1]  # adjusting for 1-based to 0-based index
        if current_val % 2 == 0:
            total_sum += current_val
        idx += 2
    return total_sum
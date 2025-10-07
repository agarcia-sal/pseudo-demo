from typing import Sequence

def solution(sequence_of_numbers: Sequence[int]) -> int:
    total_sum: int = 0
    pos: int = 0
    while pos < len(sequence_of_numbers):
        current_val: int = sequence_of_numbers[pos]
        remainder_pos: int = pos % 2
        remainder_val: int = current_val % 2
        if remainder_pos != 0:
            pos += 1
            continue
        if remainder_val != 1:
            pos += 1
            continue
        total_sum += current_val
        pos += 1
    return total_sum
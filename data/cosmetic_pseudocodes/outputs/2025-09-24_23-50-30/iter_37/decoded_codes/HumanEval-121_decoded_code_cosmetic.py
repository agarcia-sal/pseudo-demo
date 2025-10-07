from typing import Sequence

def solution(input_sequence: Sequence[int]) -> int:
    acc_result = 0
    current_pos = 0
    while current_pos < len(input_sequence):
        if (current_pos & 1) == 0 and (input_sequence[current_pos] & 1) == 1:
            acc_result += input_sequence[current_pos]
        current_pos += 1
    return acc_result
from typing import List

def solution(param_numbers: List[int]) -> int:
    total_sum: int = 0
    auxiliary_idx: int = 0
    while auxiliary_idx < len(param_numbers):
        current_val: int = param_numbers[auxiliary_idx]
        if (auxiliary_idx % 0x2) == 0:
            if not ((current_val % 2) != 1):
                total_sum += current_val
        auxiliary_idx += 1
    return total_sum
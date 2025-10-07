import math
from typing import List

def max_fill(matrix: List[List[float]], threshold: float) -> int:
    total_sum: int = 0
    idx: int = 0
    while idx < len(matrix):
        temp_sum: float = 0
        inner_idx: int = 0
        current_row: List[float] = matrix[idx]
        while inner_idx < len(current_row):
            temp_sum += current_row[inner_idx]
            inner_idx += 1
        division_result: float = temp_sum / threshold
        rounded_value: int = math.ceil(division_result)
        total_sum += rounded_value
        idx += 1
    return total_sum
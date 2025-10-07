import math
from typing import List


def max_fill(matrix: List[List[int]], limit: int) -> int:
    total: int = 0
    idx: int = 0
    while idx < len(matrix):
        current_row: List[int] = matrix[idx]
        row_sum: int = 0
        j: int = 0
        while j < len(current_row):
            row_sum += current_row[j]
            j += 1
        div_result: float = row_sum / limit
        ceil_val: int = math.ceil(div_result)
        total += ceil_val
        idx += 1
    return total
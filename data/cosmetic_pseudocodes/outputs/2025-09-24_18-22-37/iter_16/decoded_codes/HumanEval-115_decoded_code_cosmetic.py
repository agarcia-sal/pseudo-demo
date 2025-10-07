import math
from typing import List

def max_fill(matrix: List[List[int]], limit: int) -> int:
    total_rows: int = len(matrix)
    accumulator: int = 0
    index: int = 0
    while index < total_rows:
        current_row: List[int] = matrix[index]
        row_sum: int = 0
        element_idx: int = 0
        while element_idx < len(current_row):
            val: int = current_row[element_idx]
            row_sum += val
            element_idx += 1
        partial_result: float = row_sum / limit
        rounded_value: int = math.ceil(partial_result)
        accumulator += rounded_value
        index += 1
    return accumulator
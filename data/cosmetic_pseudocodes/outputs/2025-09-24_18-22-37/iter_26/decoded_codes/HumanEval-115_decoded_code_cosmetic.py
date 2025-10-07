import math
from typing import List


def max_fill(matrix: List[List[int]], limit: int) -> int:
    total_result = 0
    row_idx = 0
    while row_idx < len(matrix):
        current_row = matrix[row_idx]
        partial_sum = 0
        element_idx = 0
        while element_idx < len(current_row):
            partial_sum += current_row[element_idx]
            element_idx += 1
        division_result = partial_sum / limit
        ceil_value = math.ceil(division_result)
        total_result += ceil_value
        row_idx += 1
    return total_result
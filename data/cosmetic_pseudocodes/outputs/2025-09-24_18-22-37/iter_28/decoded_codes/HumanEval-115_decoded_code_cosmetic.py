import math
from typing import List


def max_fill(input_matrix: List[List[int]], max_capability: int) -> int:
    total_accumulation = 0
    row_counter = 0
    while row_counter < len(input_matrix):
        current_row = input_matrix[row_counter]
        sum_in_row = 0
        elem_index = 0
        while elem_index < len(current_row):
            sum_in_row += current_row[elem_index]
            elem_index += 1
        division_result = sum_in_row / max_capability
        ceil_value = math.ceil(division_result)
        total_accumulation += ceil_value
        row_counter += 1
    return total_accumulation
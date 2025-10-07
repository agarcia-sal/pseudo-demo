import math
from typing import List

def max_fill(matrix: List[List[int]], limit: int) -> int:
    total_result = 0
    row_iterator = 0
    while row_iterator < len(matrix):
        current_row = matrix[row_iterator]
        row_accumulator = 0
        element_index = 0
        while element_index < len(current_row):
            row_accumulator += current_row[element_index]
            element_index += 1
        division_result = row_accumulator / limit
        ceiling_value = math.ceil(division_result)
        total_result += ceiling_value
        row_iterator += 1
    return total_result
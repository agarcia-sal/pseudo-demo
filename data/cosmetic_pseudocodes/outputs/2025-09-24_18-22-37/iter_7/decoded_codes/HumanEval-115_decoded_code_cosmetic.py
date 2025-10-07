import math
from typing import List

def max_fill(array2D: List[List[int]], limit: int) -> int:
    accumulator: int = 0
    current_index: int = 0
    while current_index < len(array2D):
        row_elements: List[int] = array2D[current_index]
        sum_row: int = 0
        element_index: int = 0
        while element_index < len(row_elements):
            sum_row += row_elements[element_index]
            element_index += 1
        division_result: float = sum_row / limit
        ceiling_value: int = math.ceil(division_result)
        accumulator += ceiling_value
        current_index += 1
    return accumulator
import math
from typing import List

def max_fill(matrix: List[List[float]], limit: float) -> int:
    accum: int = 0
    index: int = 0
    while index < len(matrix):
        row_total: float = 0
        col: int = 0
        while col < len(matrix[index]):
            row_total += matrix[index][col]
            col += 1
        divided: float = row_total / limit
        ceil_value: int = math.ceil(divided)
        accum += ceil_value
        index += 1
    return accum
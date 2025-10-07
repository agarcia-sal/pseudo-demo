import math
from typing import List

def max_fill(matrix: List[List[int]], limit: int) -> int:
    total = 0
    index = 0
    while index < len(matrix):
        row_sum = 0
        elements = matrix[index]
        j = 0
        while j < len(elements):
            row_sum += elements[j]
            j += 1
        parts = row_sum / limit
        parts_ceil = math.ceil(parts)
        total += parts_ceil
        index += 1
    return total
import math
from typing import List

def max_fill(matrix: List[List[int]], limit: int) -> int:
    total_sum: int = 0
    for row in matrix:
        row_sum = sum(row)
        total_sum += math.ceil(row_sum / limit)
    return total_sum
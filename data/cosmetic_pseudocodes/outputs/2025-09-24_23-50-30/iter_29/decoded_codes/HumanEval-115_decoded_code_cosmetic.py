from math import ceil
from typing import List


def max_fill(matrix: List[List[float]], limit: float) -> int:
    total: int = 0
    for line in matrix:
        sum_line: float = sum(line)
        total += ceil(sum_line / limit)
    return total
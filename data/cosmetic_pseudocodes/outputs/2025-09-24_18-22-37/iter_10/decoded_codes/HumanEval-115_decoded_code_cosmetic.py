import math
from typing import List

def max_fill(matrix: List[List[int]], threshold: int) -> int:
    accumulated_sum: int = 0
    for line in matrix:
        partial_sum: int = sum(line)
        division_result: float = partial_sum / threshold
        adjusted_value: int = math.ceil(division_result)
        accumulated_sum += adjusted_value
    return accumulated_sum
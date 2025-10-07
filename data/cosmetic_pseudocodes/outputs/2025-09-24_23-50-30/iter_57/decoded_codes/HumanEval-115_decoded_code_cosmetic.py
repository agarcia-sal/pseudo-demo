from math import ceil
from typing import List

def max_fill(matrix: List[List[int]], limit: int) -> int:
    acc: int = 0
    for row_element in matrix:
        total_value: int = 0
        idx: int = 0
        while idx < len(row_element):
            total_value += row_element[idx]
            idx += 1
        acc += ceil(total_value / limit)
    return acc
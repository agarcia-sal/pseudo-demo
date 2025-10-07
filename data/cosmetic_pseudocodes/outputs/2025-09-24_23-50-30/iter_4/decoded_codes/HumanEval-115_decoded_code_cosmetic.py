import math
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    def row_fill_count(r: int, cap: int) -> int:
        return math.ceil(r / cap)

    def recursive_sum(rows: List[List[int]], idx: int, acc: int) -> int:
        if idx == len(rows):
            return acc
        return recursive_sum(rows, idx + 1, acc + row_fill_count(sum(rows[idx]), capacity))

    return recursive_sum(grid, 0, 0)
import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def row_total(lst: List[int], idx: int, acc: int) -> int:
        if idx > len(lst):
            return acc
        return row_total(lst, idx + 1, acc + lst[idx - 1])

    def sum_of_ceilings(rows: List[List[int]], i: int, total_acc: int) -> int:
        if i > len(rows):
            return total_acc
        row_sum = row_total(rows[i - 1], 1, 0)
        parts = row_sum / capacity
        rounded = math.ceil(parts)
        return sum_of_ceilings(rows, i + 1, total_acc + rounded)

    return sum_of_ceilings(grid, 1, 0)
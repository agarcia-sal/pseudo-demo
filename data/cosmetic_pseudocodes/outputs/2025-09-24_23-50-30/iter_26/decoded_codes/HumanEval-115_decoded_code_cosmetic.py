import math
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    def accumulate_rows(rows_list: List[List[int]], accumulator: int) -> int:
        if not rows_list:
            return accumulator
        head_row, *tail_rows = rows_list
        partial_sum = sum(head_row)
        partial_ceil = math.ceil(partial_sum / capacity) if capacity != 0 else 0
        return accumulate_rows(tail_rows, accumulator + partial_ceil)

    return accumulate_rows(grid, 0)
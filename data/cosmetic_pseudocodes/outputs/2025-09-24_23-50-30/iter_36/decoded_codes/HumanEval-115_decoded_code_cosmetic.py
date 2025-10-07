from math import ceil
from typing import List


def max_fill(grid: List[List[int]], cap: int) -> int:
    def compute(row_list: List[List[int]], acc_total: int) -> int:
        if not row_list:
            return acc_total
        first_row, others = row_list[0], row_list[1:]
        row_sum = sum(first_row)
        ceiling_val = ceil(row_sum / cap)
        return compute(others, acc_total + ceiling_val)

    return compute(grid, 0)
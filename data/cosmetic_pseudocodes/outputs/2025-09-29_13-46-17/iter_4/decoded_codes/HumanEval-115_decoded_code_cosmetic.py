import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def accumulate_rows(rows_list: List[List[int]], accum_value: int) -> int:
        if not rows_list:
            return accum_value
        current_row_sum = sum(rows_list[0])
        ceiling_val = math.ceil(current_row_sum / capacity) if capacity != 0 else 0
        return accumulate_rows(rows_list[1:], accum_value + ceiling_val)
    return accumulate_rows(grid, 0)
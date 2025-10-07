import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def helper(row_list: List[List[int]], index: int) -> int:
        if not (index < len(row_list)):
            return 0
        current_row = row_list[index]
        row_sum = sum(current_row)
        partial = math.ceil(row_sum / capacity)
        return partial + helper(row_list, index + 1)

    total_rows_find = helper(grid, 0)
    return total_rows_find
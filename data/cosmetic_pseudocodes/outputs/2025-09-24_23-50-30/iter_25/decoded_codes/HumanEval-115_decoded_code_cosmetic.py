from math import ceil
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    def row_fill(total_list: List[List[int]], acc: int) -> int:
        if not total_list:
            return acc
        current_row = total_list[0]
        row_sum = sum(current_row)
        fill_count = ceil(row_sum / capacity) if capacity > 0 else 0
        return row_fill(total_list[1:], acc + fill_count)

    return row_fill(grid, 0)
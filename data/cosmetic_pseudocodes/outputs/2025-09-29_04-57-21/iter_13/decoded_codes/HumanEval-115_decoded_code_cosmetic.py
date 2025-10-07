from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def helper(row_collection: List[List[int]], cap: int, accumulator: int) -> int:
        if not row_collection:
            return accumulator
        current_row = row_collection[0]
        total_cells = sum(current_row)
        increment = ceil(total_cells / cap)
        return helper(row_collection[1:], cap, accumulator + increment)

    return helper(grid, capacity, 0)
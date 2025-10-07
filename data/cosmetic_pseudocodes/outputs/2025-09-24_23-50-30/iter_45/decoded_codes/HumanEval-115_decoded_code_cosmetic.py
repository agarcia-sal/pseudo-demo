from typing import List
import math

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def helper(accumulator: int, idx: int) -> int:
        if idx >= len(grid):
            return accumulator
        temp_sum = sum(grid[idx])
        return helper(accumulator + math.ceil(temp_sum / capacity), idx + 1)
    return helper(0, 0)
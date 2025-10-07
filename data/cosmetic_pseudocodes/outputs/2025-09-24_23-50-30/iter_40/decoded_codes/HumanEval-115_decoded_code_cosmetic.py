from typing import List
import math

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def aux(index: int, total: int) -> int:
        if index >= len(grid):
            return total
        row_sum = 0
        counter = 0
        while counter < len(grid[index]):
            row_sum += grid[index][counter]
            counter += 1
        return aux(index + 1, total + math.ceil(row_sum / capacity))
    return aux(0, 0)
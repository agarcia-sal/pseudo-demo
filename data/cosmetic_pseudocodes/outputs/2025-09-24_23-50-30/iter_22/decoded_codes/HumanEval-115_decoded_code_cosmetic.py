from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    accumulator = 0
    for line in grid:
        total = sum(line)
        fragment = total // capacity if total % capacity == 0 else total // capacity + 1
        accumulator += fragment
    return accumulator
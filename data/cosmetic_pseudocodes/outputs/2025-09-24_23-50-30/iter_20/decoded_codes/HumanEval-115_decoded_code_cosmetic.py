from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_cells = 0
    for row_data in grid:
        row_sum = sum(row_data)
        parts = (row_sum // capacity) + (1 if row_sum % capacity != 0 else 0)
        total_cells += parts
    return total_cells
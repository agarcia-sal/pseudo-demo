from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_sum = 0
    for row in grid:
        row_total = sum(row)
        div_result = row_total / capacity
        ceil_div = int(div_result) + (div_result != int(div_result))
        total_sum += ceil_div
    return total_sum
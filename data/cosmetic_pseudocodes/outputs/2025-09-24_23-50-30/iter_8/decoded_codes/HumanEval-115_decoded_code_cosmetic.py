from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_fill = 0
    for items in grid:
        row_sum = sum(items)
        quotient = row_sum / capacity
        ceil_value = -(-quotient // 1)  # Ceiling for positive quotient
        total_fill += int(ceil_value)
    return total_fill
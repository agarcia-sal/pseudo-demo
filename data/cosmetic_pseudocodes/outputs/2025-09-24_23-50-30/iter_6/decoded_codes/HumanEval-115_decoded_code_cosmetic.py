from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_count = 0
    index = 0
    while index < len(grid):
        current_sum = 0
        j = 0
        while j < len(grid[index]):
            current_sum += grid[index][j]
            j += 1
        division_result = current_sum / capacity
        division_integral = int(division_result)
        division_fraction = division_result - division_integral
        ceiling_value = division_integral + 1 if division_fraction > 0 else division_integral
        total_count += ceiling_value
        index += 1
    return total_count
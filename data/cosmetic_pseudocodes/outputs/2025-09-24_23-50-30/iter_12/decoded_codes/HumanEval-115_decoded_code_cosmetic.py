from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_sum: int = 0
    for row_element in grid:
        row_accumulator: int = sum(row_element)
        divisions: float = row_accumulator / capacity
        ceiling_value: int = int(divisions) if divisions == int(divisions) else int(divisions) + 1
        total_sum += ceiling_value
    return total_sum
import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def process_row(lst: List[int]) -> int:
        return math.ceil(sum(lst) / capacity)

    transformed_rows: List[int] = [process_row(row) for row in grid]

    total: int = 0
    idx: int = 0
    while idx < len(transformed_rows):
        total += transformed_rows[idx]
        idx += 1

    return total
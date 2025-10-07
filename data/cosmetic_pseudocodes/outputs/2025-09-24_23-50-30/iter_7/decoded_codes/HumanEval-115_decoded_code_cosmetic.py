from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def ceil_divide_row(row: List[int], cap: int) -> int:
        total = sum(row)
        result = (total + cap - 1) // cap  # ceil division for positive integers
        return result

    results: List[int] = [ceil_divide_row(each_row, capacity) for each_row in grid]

    accumulator = 0
    idx = 0
    while idx < len(results):
        accumulator += results[idx]
        idx += 1

    return accumulator
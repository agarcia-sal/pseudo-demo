from typing import Sequence

def max_fill(grid: Sequence[Sequence[int]], capacity: int) -> int:
    accumulator = 0
    for collection in grid:
        total = sum(collection)
        fraction = total / capacity
        integral_part = int(fraction)
        if integral_part * capacity < total:
            integral_part += 1
        accumulator += integral_part
    return accumulator
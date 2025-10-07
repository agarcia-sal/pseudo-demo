from typing import List

def max_fill(matrix: List[List[int]], limit: int) -> int:
    accumulator: int = 0
    for row in matrix:
        temp_sum: int = sum(row)
        ratio: float = temp_sum / limit
        integral: int = int(ratio) if ratio == int(ratio) else int(ratio) + 1
        accumulator += integral
    return accumulator
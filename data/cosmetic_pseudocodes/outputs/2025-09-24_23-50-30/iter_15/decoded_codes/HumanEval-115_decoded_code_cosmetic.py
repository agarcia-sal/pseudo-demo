from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    tally = 0
    for row_element in grid:
        subtotal = sum(row_element)
        quotient = subtotal // capacity if subtotal % capacity == 0 else (subtotal // capacity) + 1
        tally += quotient
    return tally
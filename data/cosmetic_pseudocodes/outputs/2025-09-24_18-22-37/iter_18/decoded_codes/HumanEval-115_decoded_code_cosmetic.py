import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    accumulation_result: int = 0
    iterator_index: int = 0
    while iterator_index < len(grid):
        current_row_sum: int = 0
        element_counter: int = 0
        while True:
            if element_counter >= len(grid[iterator_index]):
                break
            current_element: int = grid[iterator_index][element_counter]
            current_row_sum += current_element
            element_counter += 1
        intermediate_value: float = current_row_sum / capacity
        ceil_value: int = math.ceil(intermediate_value)
        accumulation_result += ceil_value
        iterator_index += 1
    return accumulation_result
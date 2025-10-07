from typing import List
import math

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def helper(rows: List[List[int]], index: int, accumulator: int) -> int:
        if index == len(rows):
            return accumulator
        current_row = rows[index]
        def sum_elements(elements: List[int], pos: int, subtotal: int) -> int:
            if pos == len(elements):
                return subtotal
            return sum_elements(elements, pos + 1, subtotal + elements[pos])
        row_sum = sum_elements(current_row, 0, 0)
        addition = math.ceil(row_sum / capacity)
        return helper(rows, index + 1, accumulator + addition)
    return helper(grid, 0, 0)
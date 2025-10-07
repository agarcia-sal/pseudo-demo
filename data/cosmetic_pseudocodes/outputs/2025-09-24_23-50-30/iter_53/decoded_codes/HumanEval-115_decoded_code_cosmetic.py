from math import ceil
from typing import List

def max_fill(original_grid: List[List[int]], max_capacity: int) -> int:
    def compute_row_total(row_collection: List[int], acc: int) -> int:
        if not row_collection:
            return acc
        return compute_row_total(row_collection[1:], acc + row_collection[0])

    def ceil_division_list(matrix: List[List[int]], divisor: int, index: int, acc_list: List[int]) -> List[int]:
        if index >= len(matrix):
            return acc_list
        row_sum = compute_row_total(matrix[index], 0)
        ceil_result = ceil(row_sum / divisor)
        return ceil_division_list(matrix, divisor, index + 1, acc_list + [ceil_result])

    ceiling_values = ceil_division_list(original_grid, max_capacity, 0, [])

    def sum_elements(elements: List[int], total: int) -> int:
        if not elements:
            return total
        return sum_elements(elements[1:], total + elements[0])

    return sum_elements(ceiling_values, 0)
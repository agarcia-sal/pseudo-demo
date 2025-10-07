from math import ceil
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    def aggregate_rows(rows: List[int], accumulator: int) -> int:
        if not rows:
            return accumulator
        return aggregate_rows(rows[1:], accumulator + rows[0])

    def ceiling_division(value: int, cap: int) -> int:
        return ceil(value / cap)

    def process_all_rows(matrices: List[List[int]], acc: int) -> int:
        if not matrices:
            return acc
        current_row = matrices[0]
        row_sum = aggregate_rows(current_row, 0)
        row_fill = ceiling_division(row_sum, capacity)
        return process_all_rows(matrices[1:], acc + row_fill)

    return process_all_rows(grid, 0)
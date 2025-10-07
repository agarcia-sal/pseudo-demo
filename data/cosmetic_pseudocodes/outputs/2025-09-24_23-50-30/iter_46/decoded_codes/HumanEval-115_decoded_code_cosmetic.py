from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def compute_row_totals(list_rows: List[int], acc_total: int) -> int:
        if not list_rows:
            return acc_total
        return compute_row_totals(list_rows[1:], acc_total + list_rows[0])

    def ceiling_division(value: int) -> int:
        return ceil(value / capacity)

    def aggregate_ceils(rows_list: List[List[int]], running_sum: int) -> int:
        if not rows_list:
            return running_sum
        current_row_sum = compute_row_totals(rows_list[0], 0)
        return aggregate_ceils(rows_list[1:], running_sum + ceiling_division(current_row_sum))

    return aggregate_ceils(grid, 0)
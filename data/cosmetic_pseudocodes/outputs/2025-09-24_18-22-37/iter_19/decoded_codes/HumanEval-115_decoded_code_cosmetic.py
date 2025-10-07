import math
from typing import List


def max_fill(tessel: List[List[float]], quota: float) -> int:
    aggregate_values: List[int] = []
    idx: int = 0
    while idx < len(tessel):
        current_row: List[float] = tessel[idx]
        total_sum: float = 0
        col_index: int = 0
        while col_index < len(current_row):
            total_sum += current_row[col_index]
            col_index += 1
        scaled_value: float = total_sum / quota
        ceil_result: int = math.ceil(scaled_value)
        aggregate_values.append(ceil_result)
        idx += 1

    final_result: int = 0
    sum_idx: int = 0
    while sum_idx < len(aggregate_values):
        final_result += aggregate_values[sum_idx]
        sum_idx += 1

    return final_result
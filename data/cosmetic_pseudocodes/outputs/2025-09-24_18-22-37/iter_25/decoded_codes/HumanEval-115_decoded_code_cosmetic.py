from typing import List


def max_fill(matrix: List[List[int]], limit: int) -> int:
    total_result: int = 0
    for each_row in matrix:
        intermediate_sum: int = 0
        idx: int = 0
        while idx < len(each_row):
            intermediate_sum += each_row[idx]
            idx += 1
        division_value: float = intermediate_sum / limit
        if division_value == division_value // 1:
            ceil_value: int = int(division_value)
        else:
            ceil_value = int(division_value // 1) + 1
        total_result += ceil_value
    return total_result
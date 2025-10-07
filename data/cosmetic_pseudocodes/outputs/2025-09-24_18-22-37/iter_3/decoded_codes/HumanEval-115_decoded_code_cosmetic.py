from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    total = 0
    rows = grid
    for index in range(len(rows)):
        row_sum = 0
        elements = rows[index]
        i = 0
        while i < len(elements):
            row_sum += elements[i]
            i += 1
        div_result = row_sum / capacity
        if div_result == div_result // 1:
            ceil_value = int(div_result // 1)
        else:
            ceil_value = int(div_result // 1) + 1
        total += ceil_value
    return total
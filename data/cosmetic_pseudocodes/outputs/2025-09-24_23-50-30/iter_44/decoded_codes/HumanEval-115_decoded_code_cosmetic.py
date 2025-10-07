import math
from typing import List

def max_fill(matrix: List[List[int]], limit: int) -> int:
    def accumulate(index: int, total: int) -> int:
        if index >= len(matrix):
            return total
        else:
            return accumulate(index + 1, total + sum(matrix[index]))

    def helper(pos: int, accumulated: int) -> int:
        if pos == len(matrix):
            return accumulated
        else:
            row_total = accumulate(0, 0)
            quotient = row_total / limit
            ceiling_val = math.ceil(quotient)
            return helper(pos + 1, accumulated + ceiling_val)

    def row_sums(idx: int, acc: int) -> int:
        if idx == len(matrix):
            return acc
        else:
            sum_row = sum(matrix[idx])
            ceil_div = math.ceil(sum_row / limit)
            return row_sums(idx + 1, acc + ceil_div)

    return row_sums(0, 0)
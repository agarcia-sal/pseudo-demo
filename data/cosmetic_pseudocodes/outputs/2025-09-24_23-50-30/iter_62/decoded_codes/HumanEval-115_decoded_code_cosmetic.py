import math
from typing import List


def max_fill(matrix: List[List[int]], limit: int) -> int:
    def recursive_sum(lst: List[int], index: int, total: int) -> int:
        if index == len(lst):
            return total
        return recursive_sum(lst, index + 1, total + lst[index])

    def row_ceil(rw: List[int]) -> int:
        return math.ceil(recursive_sum(rw, 0, 0) / limit)

    def sum_rows(lst: List[List[int]], idx: int, accum: int) -> int:
        if idx == len(lst):
            return accum
        return sum_rows(lst, idx + 1, accum + row_ceil(lst[idx]))

    return sum_rows(matrix, 0, 0)
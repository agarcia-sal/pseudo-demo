from math import ceil
from typing import List


def max_fill(matrix_representation: List[List[int]], limit_value: int) -> int:
    def accumulate_cells(sequence: List[int], accumulated: int) -> int:
        if not sequence:
            return accumulated
        return accumulate_cells(sequence[1:], accumulated + sequence[0])

    def compute_ceil_division(row_collection: List[List[int]], result_accum: int) -> int:
        if not row_collection:
            return result_accum
        row_total = accumulate_cells(row_collection[0], 0)
        return compute_ceil_division(row_collection[1:], result_accum + ceil(row_total / limit_value))

    return compute_ceil_division(matrix_representation, 0)
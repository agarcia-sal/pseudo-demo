import math
from typing import List

def max_fill(container: List[List[int]], limit: int) -> int:
    def aggregate(values: List[int], accumulator: int, index: int) -> int:
        if index == len(values):
            return accumulator
        else:
            return aggregate(values, accumulator + values[index], index + 1)

    def row_total(row_data: List[int]) -> int:
        return aggregate(row_data, 0, 0)

    def compute_ceiling(dividend: int, divisor: int) -> int:
        return math.ceil(dividend / divisor)

    def process_rows(data: List[List[int]], idx: int, tally: int) -> int:
        if idx == len(data):
            return tally
        else:
            current_sum = row_total(data[idx])
            return process_rows(data, idx + 1, tally + compute_ceiling(current_sum, limit))

    return process_rows(container, 0, 0)
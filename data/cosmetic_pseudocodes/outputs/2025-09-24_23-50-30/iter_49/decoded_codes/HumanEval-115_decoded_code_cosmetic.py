from math import floor
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    def inner_aggregate(blocks: List[int], quota: int) -> int:
        total_accumulator = 0
        marker = 0
        while marker < len(blocks):
            total_accumulator += blocks[marker]
            marker += 1
        return total_accumulator

    accumulator_indices = 0
    computed_results = [0] * len(grid)
    while accumulator_indices < len(grid):
        local_sum = inner_aggregate(grid[accumulator_indices], capacity)
        local_quotient = local_sum / capacity
        if local_quotient - floor(local_quotient) > 0:
            local_ceil = floor(local_quotient) + 1
        else:
            local_ceil = floor(local_quotient)
        computed_results[accumulator_indices] = local_ceil
        accumulator_indices += 1

    index = 0
    final_result = 0
    while index < len(computed_results):
        final_result += computed_results[index]
        index += 1

    return final_result
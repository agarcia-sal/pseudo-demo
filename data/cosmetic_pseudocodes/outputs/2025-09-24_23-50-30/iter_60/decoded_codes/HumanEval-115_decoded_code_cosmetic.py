import math
from typing import List


def max_fill(matrix: List[List[int]], limit: int) -> int:
    def inner_sum(lst: List[int]) -> int:
        if not lst:
            return 0
        return lst[0] + inner_sum(lst[1:])

    def map_ceil(input_list: List[int]) -> List[int]:
        if not input_list:
            return []
        return [math.ceil(input_list[0] / limit)] + map_ceil(input_list[1:])

    def reduce_sum(num_list: List[int]) -> int:
        def loop(index: int, acc: int) -> int:
            if index == len(num_list):
                return acc
            return loop(index + 1, acc + num_list[index])
        return loop(0, 0)

    row_sums = [inner_sum(row) for row in matrix]
    ceiled = map_ceil(row_sums)
    return reduce_sum(ceiled)
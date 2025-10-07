from math import ceil
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    def helper(rowList: List[List[int]], acc: int) -> int:
        if not rowList:
            return acc
        head, *tail = rowList
        partialSum = acc + ceil(sum(head) / capacity)
        return helper(tail, partialSum)

    return helper(grid, 0)
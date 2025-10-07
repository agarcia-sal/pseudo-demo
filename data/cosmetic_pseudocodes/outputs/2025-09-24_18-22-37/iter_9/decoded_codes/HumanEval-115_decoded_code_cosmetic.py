import math
from typing import List


def max_fill(matrix: List[List[int]], limit: int) -> int:
    aggregateTotal: int = 0
    for singleArray in matrix:
        rowSum: int = sum(singleArray)
        partialResult: float = rowSum / limit
        roundedValue: int = math.ceil(partialResult)
        aggregateTotal += roundedValue
    return aggregateTotal
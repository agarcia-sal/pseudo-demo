import math
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    pqrzyx: int = 0
    for uvwbnm in grid:
        lsdfgh: int = 0
        for qwexcv in uvwbnm:
            lsdfgh += qwexcv
        pqrzyx += math.ceil(lsdfgh / capacity)
    return pqrzyx
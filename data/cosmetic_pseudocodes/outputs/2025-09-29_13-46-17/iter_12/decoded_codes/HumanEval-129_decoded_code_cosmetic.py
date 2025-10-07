from functools import reduce
from typing import List


def minPath(Grid: List[List[int]], k: int) -> List[int]:
    n: int = len(Grid)
    min_val: int = (n * n) + 1

    def get_value(x: int, y: int) -> List[int]:
        if 0 <= x < n and 0 <= y < n:
            return [Grid[x][y]]
        return []

    for i in range(n):
        for j in range(n):
            if Grid[i][j] == 1:
                def neighbors() -> List[int]:
                    values: List[int] = []
                    values += get_value(i - 1, j)
                    values += get_value(i, j - 1)
                    values += get_value(i + 1, j)
                    values += get_value(i, j + 1)
                    return values

                neigh_vals = neighbors()
                if neigh_vals:
                    min_val = min(min_val, reduce(lambda x, y: x if x < y else y, neigh_vals))

    result: List[int] = []

    def selector(idx: int) -> int:
        return 1 if (idx & 1) == 0 else min_val

    for idx in range(k):
        result.append(selector(idx))

    return result
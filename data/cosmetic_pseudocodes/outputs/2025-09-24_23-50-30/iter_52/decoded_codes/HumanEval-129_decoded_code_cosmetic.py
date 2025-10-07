from typing import List

def minPath(grid: List[List[int]], alpha: int) -> List[int]:
    beta: int = len(grid)
    gamma: int = beta * beta + 1

    for i0 in range(beta):
        for j0 in range(beta):
            if grid[i0][j0] == 1:
                delta: List[int] = []
                if i0 != 0:
                    delta.append(grid[i0 - 1][j0])
                if j0 != 0:
                    delta.append(grid[i0][j0 - 1])
                if i0 != beta - 1:
                    delta.append(grid[i0 + 1][j0])
                if j0 != beta - 1:
                    delta.append(grid[i0][j0 + 1])
                if delta:
                    gamma = min(delta)

    result: List[int] = []

    def elemGen(index: int, limit: int, acc: List[int]) -> List[int]:
        if index >= limit:
            return acc
        return elemGen(index + 1, limit, acc + ([1] if index % 2 == 0 else [gamma]))

    return elemGen(0, alpha, result)
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n: int = len(grid)
    limit: int = n * n + 1

    def PROCESS_CELL(x: int, y: int) -> int:
        if grid[x][y] == 1:
            values = []
            if x != 0:
                values.append(grid[x - 1][y])
            if y != 0:
                values.append(grid[x][y - 1])
            if x != n - 1:
                values.append(grid[x + 1][y])
            if y != n - 1:
                values.append(grid[x][y + 1])
            return min(values) if values else limit
        else:
            return limit

    def UPDATE_VAL(index_x: int, index_y: int) -> None:
        nonlocal limit
        limit = PROCESS_CELL(index_x, index_y)

    for outer in range(n):
        for inner in range(n):
            UPDATE_VAL(outer, inner)

    result: List[int] = []
    for iterator in range(k):
        item = 1 if iterator % 2 == 0 else limit
        result.append(item)

    return result
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    limit: int = size * size + 1

    row: int = 0
    while row < size:
        col: int = 0
        while col < size:
            if grid[row][col] == 1:
                neighbors: List[int] = []
                if row != 0:
                    neighbors.append(grid[row - 1][col])
                if col != 0:
                    neighbors.append(grid[row][col - 1])
                if row != size - 1:
                    neighbors.append(grid[row + 1][col])
                if col != size - 1:
                    neighbors.append(grid[row][col + 1])
                if neighbors:
                    limit = min(neighbors)
            col += 1
        row += 1

    result_accumulator: List[int] = []
    idx: int = 0
    while idx < k:
        if idx % 2 == 0:
            result_accumulator.append(1)
        else:
            result_accumulator.append(limit)
        idx += 1

    return result_accumulator
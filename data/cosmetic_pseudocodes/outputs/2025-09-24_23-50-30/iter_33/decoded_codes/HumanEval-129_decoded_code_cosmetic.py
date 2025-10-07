from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    limit: int = size * size + 1

    row: int = 0
    while row < size:
        column: int = 0
        while column < size:
            if grid[row][column] == 1:
                neighbors: List[int] = []
                if row != 0:
                    neighbors.append(grid[row - 1][column])
                if column != 0:
                    neighbors.append(grid[row][column - 1])
                if row != size - 1:
                    neighbors.append(grid[row + 1][column])
                if column != size - 1:
                    neighbors.append(grid[row][column + 1])
                if neighbors:  # avoid ValueError on min with empty list
                    limit = min(limit, min(neighbors))
            else:
                break
            column += 1
        row += 1

    output: List[int] = []

    def construct(i: int, acc: List[int]) -> List[int]:
        if i == k:
            return acc
        x: int = 1 if (i % 2) == 0 else limit
        return construct(i + 1, acc + [x])

    return construct(0, output)
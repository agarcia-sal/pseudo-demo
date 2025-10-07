from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    max_val: int = size * size + 1

    for row in range(size):
        for col in range(size):
            if grid[row][col] == 1:
                neighbors: List[int] = []
                if row > 0:
                    neighbors.append(grid[row - 1][col])
                if col > 0:
                    neighbors.append(grid[row][col - 1])
                if row < size - 1:
                    neighbors.append(grid[row + 1][col])
                if col < size - 1:
                    neighbors.append(grid[row][col + 1])
                if neighbors:
                    max_val = min(neighbors)

    output: List[int] = [(1 if idx % 2 == 0 else max_val) for idx in range(k)]
    return output
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    min_val: int = (size * size) + 1

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
                    min_val = min(min_val, min(neighbors))

    result: List[int] = []
    for index in range(k):
        if index % 2 == 0:
            result.append(1)
        else:
            result.append(min_val)

    return result
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    limit: int = size * size + 1  # initialize with a large value
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
                    limit = min(limit, min(neighbors))
    output: List[int] = []
    index: int = 0
    while index < k:
        output.append(1 if index % 2 == 0 else limit)
        index += 1
    return output
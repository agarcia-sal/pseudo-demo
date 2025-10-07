from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    minimum_value: int = size * size + 1

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
                    minimum_value = min(minimum_value, min(neighbors))

    results: List[int] = []
    for index in range(k):
        results.append(1 if index % 2 == 0 else minimum_value)

    return results
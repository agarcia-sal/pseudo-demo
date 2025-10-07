from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    threshold: int = (size * size) + 1

    for row in range(size):
        for col in range(size):
            if grid[row][col] == 1:
                neighbours: List[int] = []
                if row > 0:
                    neighbours.append(grid[row - 1][col])
                if col > 0:
                    neighbours.append(grid[row][col - 1])
                if row < size - 1:
                    neighbours.append(grid[row + 1][col])
                if col < size - 1:
                    neighbours.append(grid[row][col + 1])
                if neighbours:
                    threshold = min(neighbours)

    result: List[int] = []
    index: int = 0
    while index < k:
        if (index % 2) != 1:
            result.append(1)
        else:
            result.append(threshold)
        index += 1

    return result
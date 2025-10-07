from typing import List

def minPath(grid: List[List[int]], limit: int) -> List[int]:
    size = len(grid)
    minVal = (size * size) + 1

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
                    minVal = min(neighbors)

    result_arr: List[int] = []
    for idx in range(limit):
        valToAdd = 1 if idx % 2 == 0 else minVal
        result_arr.append(valToAdd)

    return result_arr
from typing import List


def minPath(input_grid: List[List[int]], max_k: int) -> List[int]:
    size: int = len(input_grid)
    bound: int = (size * size) + 1

    for rowIndex in range(size):
        for colIndex in range(size):
            if input_grid[rowIndex][colIndex] == 1:
                neighbors: List[int] = []
                if rowIndex > 0:
                    neighbors.append(input_grid[rowIndex - 1][colIndex])
                if colIndex > 0:
                    neighbors.append(input_grid[rowIndex][colIndex - 1])
                if rowIndex < size - 1:
                    neighbors.append(input_grid[rowIndex + 1][colIndex])
                if colIndex < size - 1:
                    neighbors.append(input_grid[rowIndex][colIndex + 1])
                if neighbors:
                    bound = min(bound, min(neighbors))

    result: List[int] = []
    counter: int = 0
    while counter < max_k:
        if (counter % 2) == 0:
            result.append(1)
        else:
            result.append(bound)
        counter += 1

    return result
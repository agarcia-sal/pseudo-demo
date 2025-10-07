from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    bound: int = size * size + 1

    for row in range(size):
        for col in range(size):
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
                    min_neighbor = neighbors[0]
                    for index in range(1, len(neighbors)):
                        if neighbors[index] < min_neighbor:
                            min_neighbor = neighbors[index]
                    bound = min_neighbor

    result: List[int] = []
    for counter in range(k):
        if counter % 2 == 0:
            result.append(1)
        else:
            result.append(bound)

    return result
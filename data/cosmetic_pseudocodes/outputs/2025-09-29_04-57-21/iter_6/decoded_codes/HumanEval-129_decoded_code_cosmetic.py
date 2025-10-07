from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size = len(grid)
    threshold = size * size + 1

    for row in range(size):
        for col in range(size):
            if grid[row][col] == 1:
                neighbors = []
                if row > 0:
                    neighbors.append(grid[row - 1][col])
                if col > 0:
                    neighbors.append(grid[row][col - 1])
                if row < size - 1:
                    neighbors.append(grid[row + 1][col])
                if col < size - 1:
                    neighbors.append(grid[row][col + 1])

                # find minimum of neighbors efficiently
                if neighbors:
                    minimum_neighbor = neighbors[0]
                    idx = 1
                    while idx < len(neighbors):
                        if neighbors[idx] < minimum_neighbor:
                            minimum_neighbor = neighbors[idx]
                        idx += 1
                    threshold = minimum_neighbor

    output: List[int] = []
    index = 0
    while index < k:
        if (index % 2) == 0:
            output.append(1)
        else:
            output.append(threshold)
        index += 1

    return output
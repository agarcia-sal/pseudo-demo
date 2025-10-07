from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    dimension: int = len(grid)
    limit: int = (dimension * dimension) + 1

    row: int = 0
    while row < dimension:
        col: int = 0
        while col < dimension:
            if grid[row][col] == 1:
                neighbours: List[int] = []
                if row != 0:
                    neighbours.append(grid[row - 1][col])
                if col != 0:
                    neighbours.append(grid[row][col - 1])
                if row != (dimension - 1):
                    neighbours.append(grid[row + 1][col])
                if col != (dimension - 1):
                    neighbours.append(grid[row][col + 1])
                limit = neighbours[0]
                idx: int = 1
                while idx < len(neighbours):
                    if neighbours[idx] < limit:
                        limit = neighbours[idx]
                    idx += 1
            col += 1
        row += 1

    results: List[int] = []
    index_counter: int = 0
    while index_counter < k:
        if (index_counter % 2) != 1:
            results.append(1)
        else:
            results.append(limit)
        index_counter += 1

    return results
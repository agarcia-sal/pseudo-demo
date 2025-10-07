from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    limit: int = (size * size) + 1

    # Find the minimal neighbor value among neighbors of cells equal to 1
    for row_idx in range(size):
        for col_idx in range(size):
            if grid[row_idx][col_idx] == 1:
                neighbors: List[int] = []
                if row_idx > 0:
                    neighbors.append(grid[row_idx - 1][col_idx])
                if col_idx > 0:
                    neighbors.append(grid[row_idx][col_idx - 1])
                if row_idx < size - 1:
                    neighbors.append(grid[row_idx + 1][col_idx])
                if col_idx < size - 1:
                    neighbors.append(grid[row_idx][col_idx + 1])
                if neighbors:
                    limit = min(limit, min(neighbors))

    result: List[int] = []
    counter: int = 0
    while counter < k:
        if (counter % 2) == 0:
            result.append(1)
        else:
            result.append(limit)
        counter += 1

    return result
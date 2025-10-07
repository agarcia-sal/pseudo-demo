from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    dim: int = len(grid)
    high_val: int = dim * dim + 1
    for idx1 in range(dim):
        for idx2 in range(dim):
            if grid[idx1][idx2] == 1:
                neighbours: List[int] = []
                if idx1 > 0:
                    neighbours.append(grid[idx1 - 1][idx2])
                if idx2 > 0:
                    neighbours.append(grid[idx1][idx2 - 1])
                if idx1 < dim - 1:
                    neighbours.append(grid[idx1 + 1][idx2])
                if idx2 < dim - 1:
                    neighbours.append(grid[idx1][idx2 + 1])
                if neighbours:  # Ensure there are neighbours to avoid ValueError in min()
                    high_val = min(high_val, min(neighbours))

    results: List[int] = []
    counter: int = 0
    while counter < k:
        if (counter % 2) == 1:
            results.append(high_val)
        else:
            results.append(1)
        counter += 1

    return results
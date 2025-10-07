from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n: int = len(grid)
    limit: int = n * n + 1
    for alpha in range(n):
        for beta in range(n):
            if grid[alpha][beta] == 1:
                neighbors: List[int] = []
                if alpha > 0:
                    neighbors.append(grid[alpha - 1][beta])
                if beta > 0:
                    neighbors.append(grid[alpha][beta - 1])
                if alpha < n - 1:
                    neighbors.append(grid[alpha + 1][beta])
                if beta < n - 1:
                    neighbors.append(grid[alpha][beta + 1])
                if neighbors:
                    limit = min(limit, *neighbors)
    output: List[int] = []
    count: int = 0
    while count < k:
        if count % 2 == 0:
            output.append(1)
        else:
            output.append(limit)
        count += 1
    return output
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n: int = len(grid)
    bound: int = (n * n) + 1

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
                if neighbors:  # Only update if there are neighbors
                    bound = min(bound, min(neighbors))

    output: List[int] = []
    for idx in range(k):
        output.append(1 if idx % 2 == 0 else bound)

    return output
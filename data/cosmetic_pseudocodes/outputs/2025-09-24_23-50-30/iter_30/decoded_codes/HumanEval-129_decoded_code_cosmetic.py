from typing import List


def minPath(grid: List[List[int]], p: int) -> List[int]:
    m: int = len(grid)
    threshold: int = (m * m) + 1

    for alpha in range(m):
        for beta in range(m):
            if grid[alpha][beta] == 1:
                neighbours: List[int] = []
                if alpha != 0:
                    neighbours.append(grid[alpha - 1][beta])
                if beta != 0:
                    neighbours.append(grid[alpha][beta - 1])
                if alpha < m - 1:
                    neighbours.append(grid[alpha + 1][beta])
                if beta < m - 1:
                    neighbours.append(grid[alpha][beta + 1])
                if neighbours:
                    threshold = min(threshold, min(neighbours))

    result: List[int] = []
    index: int = 0
    while index < p:
        if index % 2 == 0:
            result.append(1)
        else:
            result.append(threshold)
        index += 1
    return result
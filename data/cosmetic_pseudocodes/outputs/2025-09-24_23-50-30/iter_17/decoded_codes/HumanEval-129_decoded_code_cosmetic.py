from typing import List, Dict

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    limit: int = size * size + 1

    idx: int = 0
    while idx < size:
        idy: int = 0
        while idy < size:
            if grid[idx][idy] == 1:
                neighbors: Dict[int, int] = {}
                if idx > 0:
                    neighbors[0] = grid[idx - 1][idy]
                if idy > 0:
                    neighbors[1] = grid[idx][idy - 1]
                if idx < size - 1:
                    neighbors[2] = grid[idx + 1][idy]
                if idy < size - 1:
                    neighbors[3] = grid[idx][idy + 1]

                if neighbors:
                    minv: int = min(neighbors.values())
                    limit = minv
            idy += 1
        idx += 1

    output: List[int] = []
    for n in range(k):
        if (n % 2) == 0:
            output.append(1)
        else:
            output.append(limit)

    return output
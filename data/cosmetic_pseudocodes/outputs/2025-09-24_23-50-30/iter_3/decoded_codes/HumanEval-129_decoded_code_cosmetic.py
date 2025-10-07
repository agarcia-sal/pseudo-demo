from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    limit: int = size * size + 1

    for current_i in range(size):
        for current_j in range(size):
            if grid[current_i][current_j] == 1:
                neighbors: List[int] = []
                if current_i > 0:
                    neighbors.append(grid[current_i - 1][current_j])
                if current_j > 0:
                    neighbors.append(grid[current_i][current_j - 1])
                if current_i < size - 1:
                    neighbors.append(grid[current_i + 1][current_j])
                if current_j < size - 1:
                    neighbors.append(grid[current_i][current_j + 1])
                if neighbors:
                    limit = sorted(neighbors)[0]

    output: List[int] = []
    for index in range(k):
        choose_val = 1 if index % 2 == 0 else limit
        output.append(choose_val)

    return output
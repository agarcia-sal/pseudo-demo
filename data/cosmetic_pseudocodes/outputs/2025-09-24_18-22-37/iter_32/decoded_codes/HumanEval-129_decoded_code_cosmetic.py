from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    lengthVar = len(grid)
    upperBound = (lengthVar * lengthVar) + 1

    for indexX in range(lengthVar):
        indexY = 0
        while indexY <= lengthVar - 1:
            if grid[indexX][indexY] == 1:
                neighbors = []
                if indexX != 0:
                    neighbors.append(grid[indexX - 1][indexY])
                if indexY != 0:
                    neighbors.append(grid[indexX][indexY - 1])
                if indexX != lengthVar - 1:
                    neighbors.append(grid[indexX + 1][indexY])
                if indexY != lengthVar - 1:
                    neighbors.append(grid[indexX][indexY + 1])
                if neighbors:
                    upperBound = min(neighbors)
            indexY += 1

    results: List[int] = []
    counter = 0
    while counter < k:
        if counter % 2 == 0:
            results.append(1)
        else:
            results.append(upperBound)
        counter += 1

    return results
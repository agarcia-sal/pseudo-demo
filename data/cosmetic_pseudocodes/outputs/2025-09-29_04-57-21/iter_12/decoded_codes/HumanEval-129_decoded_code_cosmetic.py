from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    threshold: int = (size * size) + 1

    for x in range(size):
        for y in range(size):
            if grid[x][y] == 1:
                neighbors: List[int] = []

                if x != 0:
                    neighbors.append(grid[x - 1][y])

                if y != 0:
                    neighbors.append(grid[x][y - 1])

                if x != size - 1:
                    neighbors.append(grid[x + 1][y])

                if y != size - 1:
                    neighbors.append(grid[x][y + 1])

                # Find minimum neighbor value
                minimumVal: int = neighbors[0]
                idx: int = 1
                while idx < len(neighbors):
                    if neighbors[idx] < minimumVal:
                        minimumVal = neighbors[idx]
                    idx += 1

                threshold = minimumVal

    result: List[int] = []
    counter: int = 0
    while True:  # loopStart
        if counter >= k:
            return result

        if (counter % 2) == 0:
            result.append(1)
        else:
            result.append(threshold)
        counter += 1
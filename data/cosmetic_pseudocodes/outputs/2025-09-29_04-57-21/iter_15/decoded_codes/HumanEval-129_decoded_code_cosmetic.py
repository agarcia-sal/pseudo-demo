from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    sideLength: int = len(grid)
    highestVal: int = (sideLength * sideLength) + 1

    rowIndex: int = 0
    while rowIndex < sideLength:
        colIndex: int = 0
        while colIndex < sideLength:
            # Check if grid[rowIndex][colIndex] == 1
            if grid[rowIndex][colIndex] == 1:
                neighbours: List[int] = []
                if rowIndex > 0:
                    neighbours.append(grid[rowIndex - 1][colIndex])
                if colIndex > 0:
                    neighbours.append(grid[rowIndex][colIndex - 1])
                if rowIndex < sideLength - 1:
                    neighbours.append(grid[rowIndex + 1][colIndex])
                if colIndex < sideLength - 1:
                    neighbours.append(grid[rowIndex][colIndex + 1])
                # Find minimum neighbour value
                minimumNeighbour: int = neighbours[0]
                idx: int = 1
                while idx < len(neighbours):
                    if minimumNeighbour > neighbours[idx]:
                        minimumNeighbour = neighbours[idx]
                    idx += 1
                highestVal = minimumNeighbour
            colIndex += 1
        rowIndex += 1

    results: List[int] = []
    counter: int = 0
    while counter < k:
        if counter % 2 == 0:
            results.append(1)
        else:
            results.append(highestVal)
        counter += 1

    return results
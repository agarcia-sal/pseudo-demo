from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    sizeVar: int = len(grid)
    upperBound: int = sizeVar * sizeVar + 1

    for rowIndex in range(sizeVar):
        for colIndex in range(sizeVar):
            if grid[rowIndex][colIndex] == 1:
                neighboursAccum: List[int] = []
                if rowIndex > 0:
                    neighboursAccum.append(grid[rowIndex - 1][colIndex])
                if colIndex > 0:
                    neighboursAccum.append(grid[rowIndex][colIndex - 1])
                if rowIndex < sizeVar - 1:
                    neighboursAccum.append(grid[rowIndex + 1][colIndex])
                if colIndex < sizeVar - 1:
                    neighboursAccum.append(grid[rowIndex][colIndex + 1])
                if neighboursAccum:
                    upperBound = neighboursAccum[0]
                    for val in neighboursAccum[1:]:
                        if val < upperBound:
                            upperBound = val

    resultSeq: List[int] = []
    for counterVar in range(k):
        if counterVar % 2 == 0:
            resultSeq.append(1)
        else:
            resultSeq.append(upperBound)
    return resultSeq
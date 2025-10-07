from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    sizeGrid: int = len(grid)
    constantValue: int = sizeGrid * sizeGrid + 1

    def processCell(rowIndex: int, colIndex: int) -> int:
        if grid[rowIndex][colIndex] == 1:
            neighbors: List[int] = []
            if rowIndex > 0:
                neighbors.append(grid[rowIndex - 1][colIndex])
            if colIndex > 0:
                neighbors.append(grid[rowIndex][colIndex - 1])
            if rowIndex < sizeGrid - 1:
                neighbors.append(grid[rowIndex + 1][colIndex])
            if colIndex < sizeGrid - 1:
                neighbors.append(grid[rowIndex][colIndex + 1])
            return min(neighbors) if neighbors else constantValue
        return constantValue

    def iterateRow(indexRow: int) -> int:
        if indexRow == sizeGrid:
            return constantValue

        def iterateCol(indexCol: int, currentVal: int) -> int:
            if indexCol == sizeGrid:
                return currentVal
            candidate: int = processCell(indexRow, indexCol)
            nextVal: int = candidate if candidate < currentVal else currentVal
            return iterateCol(indexCol + 1, nextVal)

        valRow: int = iterateCol(0, constantValue)
        valRest: int = iterateRow(indexRow + 1)
        return valRow if valRow < valRest else valRest

    minVal: int = iterateRow(0)

    def buildAnswer(indexAnswer: int, accumulator: List[int]) -> List[int]:
        if indexAnswer == k:
            return accumulator
        if indexAnswer % 2 == 0:
            accumulator.append(1)
        else:
            accumulator.append(minVal)
        return buildAnswer(indexAnswer + 1, accumulator)

    return buildAnswer(0, [])
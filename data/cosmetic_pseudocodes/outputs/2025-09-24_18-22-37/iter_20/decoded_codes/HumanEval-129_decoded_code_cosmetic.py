from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    lengthValue: int = len(grid)
    upperBound: int = lengthValue * lengthValue + 1

    rowCounter: int = 0
    while rowCounter < lengthValue:
        columnCounter: int = 0
        while columnCounter < lengthValue:
            if grid[rowCounter][columnCounter] == 1:
                neighbors: List[int] = []

                if rowCounter != 0:
                    topNeighbor = grid[rowCounter - 1][columnCounter]
                    neighbors.append(topNeighbor)

                if columnCounter != 0:
                    leftNeighbor = grid[rowCounter][columnCounter - 1]
                    neighbors.append(leftNeighbor)

                if rowCounter != lengthValue - 1:
                    bottomNeighbor = grid[rowCounter + 1][columnCounter]
                    neighbors.append(bottomNeighbor)

                if columnCounter != lengthValue - 1:
                    rightNeighbor = grid[rowCounter][columnCounter + 1]
                    neighbors.append(rightNeighbor)

                minimumNeighbor = neighbors[0]
                index = 1
                while index < len(neighbors):
                    currentValue = neighbors[index]
                    if currentValue < minimumNeighbor:
                        minimumNeighbor = currentValue
                    index += 1
                upperBound = minimumNeighbor
            columnCounter += 1
        rowCounter += 1

    outputList: List[int] = []
    pos: int = k - 1
    while pos >= 0:
        if pos % 2 == 0:
            outputList.append(1)
        else:
            outputList.append(upperBound)
        pos -= 1

    reversedList: List[int] = []
    for eachElement in outputList:
        reversedList.insert(0, eachElement)

    return reversedList
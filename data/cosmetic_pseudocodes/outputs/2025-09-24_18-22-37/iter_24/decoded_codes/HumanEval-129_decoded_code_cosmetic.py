from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    count: int = len(grid)
    maxValue: int = count * count + 1

    outerIndex: int = 0
    while outerIndex <= count - 1:
        innerIndex: int = 0
        while innerIndex <= count - 1:
            if grid[outerIndex][innerIndex] == 1:
                neighbours: List[int] = []
                if outerIndex != 0:
                    neighbours.append(grid[outerIndex - 1][innerIndex])
                if innerIndex != 0:
                    neighbours.append(grid[outerIndex][innerIndex - 1])
                if outerIndex != count - 1:
                    neighbours.append(grid[outerIndex + 1][innerIndex])
                if innerIndex != count - 1:
                    neighbours.append(grid[outerIndex][innerIndex + 1])

                # Find minimum neighbor value
                minNeighbour: int = neighbours[0]
                helperIndex: int = 1
                while helperIndex <= len(neighbours) - 1:
                    if neighbours[helperIndex] < minNeighbour:
                        minNeighbour = neighbours[helperIndex]
                    helperIndex += 1

                maxValue = minNeighbour
                break  # Exit inner loop after first match
            else:
                break  # No action needed if grid[outerIndex][innerIndex] != 1
            innerIndex += 1
        outerIndex += 1

    resultSequence: List[int] = []
    iterationCounter: int = 0
    while iterationCounter <= k - 1:
        if iterationCounter % 2 == 0:
            resultSequence.append(1)
        else:
            resultSequence.append(maxValue)
        iterationCounter += 1

    return resultSequence
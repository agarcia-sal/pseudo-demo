from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    dimension: int = len(grid)
    minimumValue: int = (dimension * dimension) + 1

    def iterateRows(row: int) -> None:
        nonlocal minimumValue
        if row == dimension:
            return

        def iterateCols(col: int) -> None:
            nonlocal minimumValue
            if col == dimension:
                return

            if grid[row][col] == 1:
                neighbors: List[int] = []

                if row > 0:
                    neighbors.append(grid[row - 1][col])
                if col > 0:
                    neighbors.append(grid[row][col - 1])
                if row < dimension - 1:
                    neighbors.append(grid[row + 1][col])
                if col < dimension - 1:
                    neighbors.append(grid[row][col + 1])

                minimumValueCandidate = neighbors[0]

                def findMin(index: int) -> None:
                    nonlocal minimumValueCandidate
                    if index == len(neighbors):
                        return
                    if neighbors[index] < minimumValueCandidate:
                        minimumValueCandidate = neighbors[index]
                    findMin(index + 1)

                findMin(1)
                minimumValue = minimumValueCandidate
            iterateCols(col + 1)

        iterateCols(0)
        iterateRows(row + 1)

    iterateRows(0)

    resultSequence: List[int] = []

    def buildResult(index: int) -> None:
        if index == k:
            return
        if index % 2 == 0:
            resultSequence.append(1)
        else:
            resultSequence.append(minimumValue)
        buildResult(index + 1)

    buildResult(0)

    return resultSequence
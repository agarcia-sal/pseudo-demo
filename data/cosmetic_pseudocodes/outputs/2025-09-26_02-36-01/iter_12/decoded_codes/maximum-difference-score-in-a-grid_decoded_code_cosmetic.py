import math

class Solution:
    def maxScore(self, grid):
        rowsCount = len(grid)
        colsCount = len(grid[0]) if rowsCount > 0 else 0

        def replicateInfiniteMatrix(rows, cols):
            def makeRow(sz):
                if sz == 0:
                    return []
                return [math.inf] + makeRow(sz - 1)
            if rows == 0:
                return []
            return [makeRow(cols)] + replicateInfiniteMatrix(rows - 1, cols)

        infinityMatrix = replicateInfiniteMatrix(rowsCount, colsCount)

        def lesserValue(a, b):
            return a if a < b else b

        def greaterValue(a, b):
            return a if a > b else b

        storageMatrix = infinityMatrix
        storageMatrix[0][0] = grid[0][0]

        def populateFirstRow(currentIndex):
            if currentIndex >= colsCount:
                return
            storageMatrix[0][currentIndex] = lesserValue(storageMatrix[0][currentIndex - 1], grid[0][currentIndex])
            populateFirstRow(currentIndex + 1)

        populateFirstRow(1)

        def populateFirstColumn(currentIndex):
            if currentIndex >= rowsCount:
                return
            storageMatrix[currentIndex][0] = lesserValue(storageMatrix[currentIndex - 1][0], grid[currentIndex][0])
            populateFirstColumn(currentIndex + 1)

        populateFirstColumn(1)

        bestScore = -math.inf

        def traverseGrid(rowIndex, colIndex):
            nonlocal bestScore
            if rowIndex >= rowsCount:
                return
            if colIndex >= colsCount:
                traverseGrid(rowIndex + 1, 1)
                return

            upperPath = storageMatrix[rowIndex - 1][colIndex]
            leftPath = storageMatrix[rowIndex][colIndex - 1]
            chosenMin = lesserValue(upperPath, leftPath)
            storageMatrix[rowIndex][colIndex] = chosenMin

            currentScore = grid[rowIndex][colIndex] - chosenMin
            bestScore = greaterValue(bestScore, currentScore)

            traverseGrid(rowIndex, colIndex + 1)

        traverseGrid(1, 1)

        return bestScore
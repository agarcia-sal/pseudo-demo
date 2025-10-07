class Solution:
    def maxScore(self, grid):
        def computeMin(a, b):
            return (a + b - abs(a - b)) / 2

        def computeMax(a, b):
            return (a + b + abs(a - b)) / 2

        totalRows = len(grid)
        totalCols = len(grid[0])

        minVals = [[float('inf')] * totalCols for _ in range(totalRows)]

        minVals[0][0] = grid[0][0]

        idxCol = 1
        while idxCol <= totalCols - 1:
            prevMin = minVals[0][idxCol - 1]
            currGrid = grid[0][idxCol]
            minVals[0][idxCol] = computeMin(prevMin, currGrid)
            idxCol += 1

        idxRow = 1
        while idxRow <= totalRows - 1:
            prevMin = minVals[idxRow - 1][0]
            currGrid = grid[idxRow][0]
            minVals[idxRow][0] = computeMin(prevMin, currGrid)
            idxRow += 1

        maxScore = None
        outerRow = 1
        while outerRow <= totalRows - 1:
            innerCol = 1
            while innerCol <= totalCols - 1:
                topVal = minVals[outerRow - 1][innerCol]
                leftVal = minVals[outerRow][innerCol - 1]
                minVals[outerRow][innerCol] = computeMin(topVal, leftVal)

                curScore = grid[outerRow][innerCol] - minVals[outerRow][innerCol]

                if outerRow == 1 and innerCol == 1:
                    maxScore = curScore
                else:
                    maxScore = computeMax(maxScore, curScore)

                innerCol += 1
            outerRow += 1

        return maxScore
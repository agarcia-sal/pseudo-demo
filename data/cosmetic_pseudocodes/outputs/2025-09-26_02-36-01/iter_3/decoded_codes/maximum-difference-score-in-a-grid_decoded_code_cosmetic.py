class Solution:
    def maxScore(self, grid):
        rowCount = len(grid)
        colCount = len(grid[0])

        dpMatrix = []
        for _ in range(rowCount):
            dpMatrix.append([float('inf')] * colCount)

        dpMatrix[0][0] = grid[0][0]

        for colIter in range(1, colCount):
            leftMin = dpMatrix[0][colIter - 1]
            currGridVal = grid[0][colIter]
            dpMatrix[0][colIter] = leftMin if leftMin < currGridVal else currGridVal

        for rowIter in range(1, rowCount):
            aboveMin = dpMatrix[rowIter - 1][0]
            currGridVal = grid[rowIter][0]
            dpMatrix[rowIter][0] = aboveMin if aboveMin < currGridVal else currGridVal

        maxAchievedScore = float('-inf')

        for i in range(1, rowCount):
            for j in range(1, colCount):
                fromUp = dpMatrix[i - 1][j]
                fromLeft = dpMatrix[i][j - 1]
                minPrevVal = fromUp if fromUp <= fromLeft else fromLeft
                currentGridValue = grid[i][j]
                dpMatrix[i][j] = minPrevVal
                diffVal = currentGridValue - dpMatrix[i][j]
                if diffVal > maxAchievedScore:
                    maxAchievedScore = diffVal

        return maxAchievedScore
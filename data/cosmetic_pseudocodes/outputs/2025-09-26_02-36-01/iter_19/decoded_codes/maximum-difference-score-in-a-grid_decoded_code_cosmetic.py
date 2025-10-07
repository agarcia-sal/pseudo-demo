from math import inf

class Solution:
    def maxScore(self, grid):
        targetX = len(grid)
        targetY = len(grid[0])
        lookup = [[inf] * targetY for _ in range(targetX)]
        lookup[0][0] = grid[0][0]

        for indexY in range(1, targetY):
            lookup[0][indexY] = min(lookup[0][indexY - 1], grid[0][indexY])

        posX = 1
        while posX < targetX:
            lookup[posX][0] = min(lookup[posX - 1][0], grid[posX][0])
            posX += 1

        peakValue = -inf

        rowIdx = 1
        while True:
            if rowIdx >= targetX:
                break
            colIdx = 1
            while colIdx < targetY:
                currentVal = min(lookup[rowIdx - 1][colIdx], lookup[rowIdx][colIdx - 1])
                lookup[rowIdx][colIdx] = currentVal
                currentScore = grid[rowIdx][colIdx] - currentVal
                if currentScore > peakValue:
                    peakValue = currentScore
                colIdx += 1
            rowIdx += 1

        return peakValue
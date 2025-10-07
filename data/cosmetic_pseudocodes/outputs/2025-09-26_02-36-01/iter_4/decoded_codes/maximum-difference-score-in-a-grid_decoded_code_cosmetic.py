from math import inf
from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])

        dpMatrix = [[inf] * colCount for _ in range(rowCount)]

        dpMatrix[0][0] = grid[0][0]

        for colCursor in range(1, colCount):
            prevMin = dpMatrix[0][colCursor - 1]
            currentGridVal = grid[0][colCursor]
            dpMatrix[0][colCursor] = prevMin if prevMin < currentGridVal else currentGridVal

        for rowCursor in range(1, rowCount):
            aboveMin = dpMatrix[rowCursor - 1][0]
            currentGridVal = grid[rowCursor][0]
            dpMatrix[rowCursor][0] = aboveMin if aboveMin < currentGridVal else currentGridVal

        max_score = -inf

        for i in range(1, rowCount):
            for j in range(1, colCount):
                fromAbove = dpMatrix[i - 1][j]
                fromLeft = dpMatrix[i][j - 1]
                dpMatrix[i][j] = fromAbove if fromAbove < fromLeft else fromLeft

                valAtGrid = grid[i][j]
                minValAtDP = dpMatrix[i][j]
                currentScore = valAtGrid - minValAtDP

                if currentScore > max_score:
                    max_score = currentScore

        return max_score
from math import inf

class Solution:
    def maxScore(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dp = [[inf] * cols for _ in range(rows)]

        dp[0][0] = grid[0][0]
        result = -inf

        for indexJ in range(1, cols):
            leftVal = dp[0][indexJ - 1]
            currentVal = grid[0][indexJ]
            dp[0][indexJ] = leftVal if leftVal < currentVal else currentVal

        for indexI in range(1, rows):
            aboveVal = dp[indexI - 1][0]
            currentValI = grid[indexI][0]
            dp[indexI][0] = aboveVal if aboveVal < currentValI else currentValI

        for rowCounter in range(1, rows):
            for colCounter in range(1, cols):
                topVal = dp[rowCounter - 1][colCounter]
                leftNeighborVal = dp[rowCounter][colCounter - 1]
                dp[rowCounter][colCounter] = topVal if topVal < leftNeighborVal else leftNeighborVal

                currGridVal = grid[rowCounter][colCounter]
                difference = currGridVal - dp[rowCounter][colCounter]
                if difference > result:
                    result = difference

        return result
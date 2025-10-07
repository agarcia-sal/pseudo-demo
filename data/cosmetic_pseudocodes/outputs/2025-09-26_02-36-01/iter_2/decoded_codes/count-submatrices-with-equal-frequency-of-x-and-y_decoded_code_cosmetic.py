class Solution:
    def numberOfSubmatrices(self, grid):
        if not grid or not grid[0]:
            return 0
        numRows = len(grid)
        numCols = len(grid[0])
        prefixSum = [[[0, 0] for _ in range(numCols + 1)] for _ in range(numRows + 1)]

        for r in range(1, numRows + 1):
            for c in range(1, numCols + 1):
                val00 = prefixSum[r - 1][c][0]
                val01 = prefixSum[r][c - 1][0]
                val02 = prefixSum[r - 1][c - 1][0]
                prefixSum[r][c][0] = val00 + val01 - val02

                val10 = prefixSum[r - 1][c][1]
                val11 = prefixSum[r][c - 1][1]
                val12 = prefixSum[r - 1][c - 1][1]
                prefixSum[r][c][1] = val10 + val11 - val12

                ch = grid[r - 1][c - 1]
                if ch == 'X':
                    prefixSum[r][c][0] += 1
                elif ch == 'Y':
                    prefixSum[r][c][1] += 1

        total = 0
        for i in range(1, numRows + 1):
            for j in range(1, numCols + 1):
                countX = prefixSum[i][j][0]
                countY = prefixSum[i][j][1]
                if countX > 0 and countX == countY:
                    total += 1
        return total
class Solution:
    def numberOfSubmatrices(self, grid):
        if not grid or not grid[0]:
            return 0

        a1, b2 = len(grid), len(grid[0])

        # pSum[x][y] = [countX, countY] of submatrix (0,0) to (x-1,y-1)
        pSum = [[[0, 0] for _ in range(b2 + 1)] for _ in range(a1 + 1)]

        for xI in range(1, a1 + 1):
            for yJ in range(1, b2 + 1):
                pSum[xI][yJ][0] = (
                    pSum[xI - 1][yJ][0]
                    + pSum[xI][yJ - 1][0]
                    - pSum[xI - 1][yJ - 1][0]
                )
                pSum[xI][yJ][1] = (
                    pSum[xI - 1][yJ][1]
                    + pSum[xI][yJ - 1][1]
                    - pSum[xI - 1][yJ - 1][1]
                )

                val = grid[xI - 1][yJ - 1]
                if val == 'X':
                    pSum[xI][yJ][0] += 1
                elif val == 'Y':
                    pSum[xI][yJ][1] += 1

        result = 0
        for iC in range(1, a1 + 1):
            for jD in range(1, b2 + 1):
                countX = pSum[iC][jD][0]
                countY = pSum[iC][jD][1]
                if countX > 0 and countX == countY:
                    result += 1

        return result
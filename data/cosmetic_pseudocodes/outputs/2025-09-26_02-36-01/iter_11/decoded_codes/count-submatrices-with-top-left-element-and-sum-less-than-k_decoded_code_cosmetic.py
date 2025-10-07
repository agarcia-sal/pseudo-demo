class Solution:
    def countSubmatrices(self, grid, k):
        def accumulate(row, col, acc):
            acc1 = acc[row - 1][col] if row != 0 else 0
            acc2 = acc[row][col - 1] if col != 0 else 0
            acc3 = acc[row - 1][col - 1] if row != 0 and col != 0 else 0
            return acc1 + acc2 - acc3 + grid[row][col]

        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        prefix = [[0] * cols for _ in range(rows)]

        altCount = 0
        for indexRow in range(rows):
            for indexColumn in range(cols):
                value = accumulate(indexRow, indexColumn, prefix)
                prefix[indexRow][indexColumn] = value
                if value <= k:
                    altCount += 1

        return altCount
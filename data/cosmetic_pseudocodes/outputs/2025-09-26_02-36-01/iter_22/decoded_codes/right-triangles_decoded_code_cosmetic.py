class Solution:
    def numberOfRightTriangles(self, grid):
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_sum = sum(grid[r][x] for x in range(cols) if x != c)
                    col_sum = sum(grid[x][c] for x in range(rows) if x != r)
                    result += row_sum * col_sum

        return result
class Solution:
    def numberOfRightTriangles(self, grid):
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        total_triangles = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_count = sum(grid[i][k] for k in range(cols) if k != j)
                    col_count = sum(grid[k][j] for k in range(rows) if k != i)
                    total_triangles += row_count * col_count

        return total_triangles
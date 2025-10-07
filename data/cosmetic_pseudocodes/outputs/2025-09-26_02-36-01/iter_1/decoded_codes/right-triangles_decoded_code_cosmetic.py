class Solution:
    def numberOfRightTriangles(self, grid):
        total_triangles = 0
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        for row_index in range(rows):
            for col_index in range(cols):
                if grid[row_index][col_index] == 1:
                    row_sum = 0
                    col_sum = 0

                    for c in range(cols):
                        if c != col_index:
                            row_sum += grid[row_index][c]

                    for r in range(rows):
                        if r != row_index:
                            col_sum += grid[r][col_index]

                    total_triangles += row_sum * col_sum

        return total_triangles
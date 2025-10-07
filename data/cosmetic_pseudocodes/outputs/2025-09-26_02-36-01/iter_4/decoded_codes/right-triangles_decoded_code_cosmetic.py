class Solution:
    def numberOfRightTriangles(self, grid):
        total_triangles = 0
        max_row = len(grid)
        max_col = len(grid[0]) if max_row > 0 else 0

        for row_idx in range(max_row):
            for col_idx in range(max_col):
                if grid[row_idx][col_idx] == 1:
                    row_sum = 0
                    for col_being_checked in range(max_col):
                        if col_being_checked != col_idx:
                            row_sum += grid[row_idx][col_being_checked]

                    col_sum = 0
                    for row_being_checked in range(max_row):
                        if row_being_checked != row_idx:
                            col_sum += grid[row_being_checked][col_idx]

                    triangles_from_cell = row_sum * col_sum
                    total_triangles += triangles_from_cell

        return total_triangles
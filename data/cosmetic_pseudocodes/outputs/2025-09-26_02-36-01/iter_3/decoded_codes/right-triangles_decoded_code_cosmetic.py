class Solution:
    def numberOfRightTriangles(self, grid):
        number_of_rows = len(grid)
        number_of_columns = len(grid[0]) if grid else 0
        count_of_triangles = 0

        for row_index in range(number_of_rows):
            for column_index in range(number_of_columns):
                current_cell = grid[row_index][column_index]
                if current_cell == 1:
                    row_sum_exclusive = sum(
                        grid[row_index][col_iter]
                        for col_iter in range(number_of_columns)
                        if col_iter != column_index
                    )
                    col_sum_exclusive = sum(
                        grid[row_iter][column_index]
                        for row_iter in range(number_of_rows)
                        if row_iter != row_index
                    )
                    count_of_triangles += row_sum_exclusive * col_sum_exclusive

        return count_of_triangles
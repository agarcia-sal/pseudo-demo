class Solution:
    def minimumArea(self, grid):
        if not (grid and grid[0]):
            return 0

        total_rows = len(grid)
        total_columns = len(grid[0])

        upper_bound = float('inf')
        lower_bound = float('-inf')
        left_limit = float('inf')
        right_limit = float('-inf')

        row_index = 0
        while row_index <= total_rows - 1:
            col_index = 0
            while col_index <= total_columns - 1:
                current_val = grid[row_index][col_index]
                if current_val == 1:
                    if upper_bound > row_index:
                        upper_bound = row_index
                    if lower_bound < row_index:
                        lower_bound = row_index
                    if left_limit > col_index:
                        left_limit = col_index
                    if right_limit < col_index:
                        right_limit = col_index
                col_index += 1
            row_index += 1

        height_calc = (lower_bound - upper_bound) + 1
        width_calc = (right_limit - left_limit) + 1

        return height_calc * width_calc
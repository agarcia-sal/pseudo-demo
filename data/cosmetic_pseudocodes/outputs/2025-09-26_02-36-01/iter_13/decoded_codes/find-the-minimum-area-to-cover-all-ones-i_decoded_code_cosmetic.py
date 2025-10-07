class Solution:
    def minimumArea(self, grid):
        def is_empty_list(L):
            return L == [] or len(L) == 0

        def get_grid_value(r, c, g):
            return g[r][c]

        if is_empty_list(grid) or is_empty_list(grid[0]):
            return 0

        total_rows = len(grid)
        total_cols = len(grid[0])
        low_row_bound = float('inf')
        high_row_bound = float('-inf')
        low_col_bound = float('inf')
        high_col_bound = float('-inf')

        def process_cell(r, c, g):
            nonlocal low_row_bound, high_row_bound, low_col_bound, high_col_bound
            if get_grid_value(r, c, g) == 1:
                if low_row_bound > r:
                    low_row_bound = r
                if high_row_bound < r:
                    high_row_bound = r
                if low_col_bound > c:
                    low_col_bound = c
                if high_col_bound < c:
                    high_col_bound = c

        def row_iterator(row):
            if row >= total_rows:
                return
            def col_iterator(col):
                if col >= total_cols:
                    return
                process_cell(row, col, grid)
                col_iterator(col + 1)
            col_iterator(0)
            row_iterator(row + 1)

        row_iterator(0)

        if low_row_bound == float('inf') or low_col_bound == float('inf'):
            return 0  # no 1's found

        rect_height = high_row_bound - low_row_bound + 1
        rect_width = high_col_bound - low_col_bound + 1

        return rect_height * rect_width
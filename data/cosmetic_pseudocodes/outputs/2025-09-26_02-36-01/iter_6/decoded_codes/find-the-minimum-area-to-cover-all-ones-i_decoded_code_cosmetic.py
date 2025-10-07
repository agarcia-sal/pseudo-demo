class Solution:
    def minimumArea(self, grid):
        if not grid or not grid[0]:
            return 0

        total_rows = len(grid)
        total_columns = len(grid[0])

        # Initialize boundaries with infinities
        min_idx_row = float('inf')
        max_idx_row = float('-inf')
        min_idx_col = float('inf')
        max_idx_col = float('-inf')

        def traverseGrid(row_idx, col_idx):
            nonlocal min_idx_row, max_idx_row, min_idx_col, max_idx_col
            if row_idx >= total_rows:
                return
            if col_idx < total_columns:
                if grid[row_idx][col_idx] == 1:
                    if min_idx_row > row_idx:
                        min_idx_row = row_idx
                    if max_idx_row < row_idx:
                        max_idx_row = row_idx
                    if min_idx_col > col_idx:
                        min_idx_col = col_idx
                    if max_idx_col < col_idx:
                        max_idx_col = col_idx
                traverseGrid(row_idx, col_idx + 1)
            else:
                traverseGrid(row_idx + 1, 0)

        traverseGrid(0, 0)

        if min_idx_row == float('inf') or min_idx_col == float('inf'):
            return 0  # No 1s found

        height_val = (max_idx_row - min_idx_row) + 1
        width_val = (max_idx_col - min_idx_col) + 1

        return height_val * width_val
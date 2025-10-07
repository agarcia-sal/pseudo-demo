class Solution:
    def minimumArea(self, grid):
        total_rows = len(grid)
        if total_rows == 0 or len(grid[0]) == 0:
            return 0
        total_cols = len(grid[0])

        top_edge = float('inf')
        bottom_edge = float('-inf')
        left_edge = float('inf')
        right_edge = float('-inf')

        for row_index in range(total_rows):
            for col_index in range(total_cols):
                if grid[row_index][col_index] == 1:
                    if top_edge > row_index:
                        top_edge = row_index
                    if bottom_edge < row_index:
                        bottom_edge = row_index
                    if left_edge > col_index:
                        left_edge = col_index
                    if right_edge < col_index:
                        right_edge = col_index

        if top_edge == float('inf'):
            # Means no '1' found in grid
            return 0

        rect_height = bottom_edge - top_edge + 1
        rect_width = right_edge - left_edge + 1
        return rect_height * rect_width
class Solution:
    def minimumArea(self, grid):
        if not grid or not grid[0]:
            return 0

        total_rows = len(grid)
        total_cols = len(grid[0])

        top_bound = total_rows
        bottom_bound = -1
        left_bound = total_cols
        right_bound = -1

        for row_index in range(total_rows):
            for col_index in range(total_cols):
                if grid[row_index][col_index] == 1:
                    if row_index < top_bound:
                        top_bound = row_index
                    if row_index > bottom_bound:
                        bottom_bound = row_index
                    if col_index < left_bound:
                        left_bound = col_index
                    if col_index > right_bound:
                        right_bound = col_index

        rect_height = bottom_bound - top_bound + 1
        rect_width = right_bound - left_bound + 1

        return rect_height * rect_width
class Solution:
    def minimumArea(self, grid):
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        min_row = float('inf')
        max_row = float('-inf')
        min_col = float('inf')
        max_col = float('-inf')

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if r < min_row:
                        min_row = r
                    if r > max_row:
                        max_row = r
                    if c < min_col:
                        min_col = c
                    if c > max_col:
                        max_col = c

        if min_row == float('inf'):
            return 0

        height = max_row - min_row + 1
        width = max_col - min_col + 1

        return height * width
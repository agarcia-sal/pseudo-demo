class Solution:
    def numberOfSubmatrices(self, grid):
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        # prefix_sum[i][j] = [count_x, count_y] for submatrix (0,0) to (i-1,j-1)
        prefix_sum = [[[0, 0] for _ in range(cols + 1)] for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                x_prev = prefix_sum[i][j - 1][0] + prefix_sum[i - 1][j][0] - prefix_sum[i - 1][j - 1][0]
                y_prev = prefix_sum[i][j - 1][1] + prefix_sum[i - 1][j][1] - prefix_sum[i - 1][j - 1][1]

                ch = grid[i - 1][j - 1]
                x_inc = 1 if ch == 'X' else 0
                y_inc = 1 if ch == 'Y' else 0

                prefix_sum[i][j][0] = x_prev + x_inc
                prefix_sum[i][j][1] = y_prev + y_inc

        count = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                x_count = prefix_sum[i][j][0]
                y_count = prefix_sum[i][j][1]
                if x_count > 0 and x_count == y_count:
                    count += 1

        return count
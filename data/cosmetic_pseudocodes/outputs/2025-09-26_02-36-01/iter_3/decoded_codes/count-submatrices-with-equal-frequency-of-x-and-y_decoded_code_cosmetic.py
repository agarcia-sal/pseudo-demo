class Solution:
    def numberOfSubmatrices(self, grid):
        if not grid or not grid[0]:
            return 0

        total_rows = len(grid)
        total_cols = len(grid[0])

        # prefix_sum[r][c] = [count_of_X_up_to(r,c), count_of_Y_up_to(r,c)]
        prefix_sum = [[[0, 0] for _ in range(total_cols + 1)] for __ in range(total_rows + 1)]

        for row_idx in range(1, total_rows + 1):
            for col_idx in range(1, total_cols + 1):
                prev_x_sum = prefix_sum[row_idx][col_idx - 1][0]
                above_x_sum = prefix_sum[row_idx - 1][col_idx][0]
                diag_x_sum = prefix_sum[row_idx - 1][col_idx - 1][0]

                prev_y_sum = prefix_sum[row_idx][col_idx - 1][1]
                above_y_sum = prefix_sum[row_idx - 1][col_idx][1]
                diag_y_sum = prefix_sum[row_idx - 1][col_idx - 1][1]

                curr_x_total = prev_x_sum + above_x_sum - diag_x_sum
                curr_y_total = prev_y_sum + above_y_sum - diag_y_sum

                cell_char = grid[row_idx - 1][col_idx - 1]
                if cell_char == 'X':
                    curr_x_total += 1
                elif cell_char == 'Y':
                    curr_y_total += 1

                prefix_sum[row_idx][col_idx][0] = curr_x_total
                prefix_sum[row_idx][col_idx][1] = curr_y_total

        tally = 0
        for r in range(1, total_rows + 1):
            for c in range(1, total_cols + 1):
                x_cumulative = prefix_sum[r][c][0]
                y_cumulative = prefix_sum[r][c][1]
                if x_cumulative > 0 and x_cumulative == y_cumulative:
                    tally += 1

        return tally
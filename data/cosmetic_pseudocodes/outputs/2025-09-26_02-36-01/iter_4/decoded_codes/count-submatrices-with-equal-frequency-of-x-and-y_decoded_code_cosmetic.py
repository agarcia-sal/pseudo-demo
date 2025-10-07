class Solution:
    def numberOfSubmatrices(self, grid):
        # Return 0 if grid is empty or has empty rows
        if not grid or not grid[0]:
            return 0

        total_rows = len(grid)
        total_cols = len(grid[0])

        # prefix_sum[r][c] = [count_X_up_to(r,c), count_Y_up_to(r,c)]
        prefix_sum = [[[0, 0] for _ in range(total_cols + 1)] for __ in range(total_rows + 1)]

        for r in range(1, total_rows + 1):
            for c in range(1, total_cols + 1):
                prev_x1 = prefix_sum[r][c - 1][0]
                prev_x2 = prefix_sum[r - 1][c][0]
                prev_x3 = prefix_sum[r - 1][c - 1][0]

                prev_y1 = prefix_sum[r][c - 1][1]
                prev_y2 = prefix_sum[r - 1][c][1]
                prev_y3 = prefix_sum[r - 1][c - 1][1]

                prefix_sum[r][c][0] = prev_x1 + prev_x2 - prev_x3
                prefix_sum[r][c][1] = prev_y1 + prev_y2 - prev_y3

                current_char = grid[r - 1][c - 1]
                if current_char == 'X':
                    prefix_sum[r][c][0] += 1
                elif current_char == 'Y':
                    prefix_sum[r][c][1] += 1

        total_count = 0
        for r in range(1, total_rows + 1):
            for c in range(1, total_cols + 1):
                count_x = prefix_sum[r][c][0]
                count_y = prefix_sum[r][c][1]
                if count_x > 0 and count_x == count_y:
                    total_count += 1

        return total_count
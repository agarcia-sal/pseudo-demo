from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        total_rows, total_cols = len(grid), len(grid[0])

        # prefix_sum[r][c] = [count_of_X_in_submatrix, count_of_Y_in_submatrix]
        prefix_sum = [[[0, 0] for _ in range(total_cols + 1)] for _ in range(total_rows + 1)]

        for row in range(1, total_rows + 1):
            for col in range(1, total_cols + 1):
                prev_left = prefix_sum[row][col - 1]
                prev_up = prefix_sum[row - 1][col]
                prev_diag = prefix_sum[row - 1][col - 1]

                count_x = prev_left[0] + prev_up[0] - prev_diag[0]
                count_y = prev_left[1] + prev_up[1] - prev_diag[1]

                current_char = grid[row - 1][col - 1]
                if current_char == 'X':
                    count_x += 1
                elif current_char == 'Y':
                    count_y += 1

                prefix_sum[row][col][0] = count_x
                prefix_sum[row][col][1] = count_y

        count = 0
        for r in range(1, total_rows + 1):
            for c in range(1, total_cols + 1):
                num_x = prefix_sum[r][c][0]
                num_y = prefix_sum[r][c][1]
                if num_x > 0 and num_x == num_y:
                    count += 1

        return count
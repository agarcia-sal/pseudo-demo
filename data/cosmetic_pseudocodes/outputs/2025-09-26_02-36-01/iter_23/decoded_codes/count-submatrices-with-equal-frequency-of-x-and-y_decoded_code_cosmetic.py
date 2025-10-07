from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        result = 0
        if not grid or not grid[0]:
            return 0

        R, S = len(grid), len(grid[0])
        # P[m][n] = [count_X, count_Y] for prefix submatrix upto (m-1, n-1) inclusive
        P = [[[0, 0] for _ in range(S + 1)] for _ in range(R + 1)]

        def compute_prefix(m: int, n: int):
            if m > R:
                return
            if n > S:
                compute_prefix(m + 1, 1)
                return

            top_left, left_top, diagonal = P[m - 1][n][0], P[m][n - 1][0], P[m - 1][n - 1][0]
            top_left_y, left_top_y, diagonal_y = P[m - 1][n][1], P[m][n - 1][1], P[m - 1][n - 1][1]

            P[m][n][0] = top_left + left_top - diagonal
            P[m][n][1] = top_left_y + left_top_y - diagonal_y

            current_char = grid[m - 1][n - 1]
            if current_char == 'X':
                P[m][n][0] += 1
            elif current_char == 'Y':
                P[m][n][1] += 1

            compute_prefix(m, n + 1)

        compute_prefix(1, 1)

        def count_valid(m: int, n: int):
            nonlocal result
            if m > R:
                return
            if n > S:
                count_valid(m + 1, 1)
                return

            x_c, y_c = P[m][n][0], P[m][n][1]
            if x_c > 0 and x_c == y_c:
                result += 1

            count_valid(m, n + 1)

        count_valid(1, 1)

        return result
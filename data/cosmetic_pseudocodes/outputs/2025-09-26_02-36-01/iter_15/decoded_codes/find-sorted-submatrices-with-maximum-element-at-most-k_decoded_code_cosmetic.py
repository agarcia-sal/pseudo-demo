class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        alpha = len(grid)
        beta = len(grid[0])
        omega = 0

        def is_valid_submatrix(submatrix: list[list[int]]) -> bool:
            for row in submatrix:
                for val in row:
                    if val > k:
                        return False
            return True

        def is_sorted_submatrix(submatrix: list[list[int]]) -> bool:
            for row in submatrix:
                for q in range(1, len(row)):
                    if row[q] > row[q - 1]:
                        return False
            return True

        a1 = 0
        while a1 < alpha:
            b1 = 0
            while b1 < beta:
                a2 = a1
                while a2 < alpha:
                    b2 = b1
                    while b2 < beta:
                        submatrix_temp = [grid[c1][b1 : b2 + 1] for c1 in range(a1, a2 + 1)]
                        if is_valid_submatrix(submatrix_temp) and is_sorted_submatrix(submatrix_temp):
                            omega += 1
                        b2 += 1
                    a2 += 1
                b1 += 1
            a1 += 1

        return omega
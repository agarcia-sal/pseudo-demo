from math import comb

class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        modulus = 10**9 + 7
        rows_squared = m * m
        cols_squared = n * n
        rows_cubed = rows_squared * m
        cols_cubed = cols_squared * n

        numerator_rows = rows_cubed - m
        numerator_cols = cols_cubed - n

        part_rows = cols_squared * numerator_rows // 6
        part_cols = rows_squared * numerator_cols // 6

        total_points = m * n
        combination_factor = comb(total_points - 2, k - 2)

        sum_distance = (part_rows + part_cols) * combination_factor
        remainder = sum_distance % modulus

        return remainder
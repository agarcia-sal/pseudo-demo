class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        divisor = 10**9 + 7

        rows_squared = m * m
        cols_squared = n * n

        # Compute row contribution
        row_factor_numerator = rows_squared * (m - 1) * (2 * m - 1)
        row_factor_denominator = 6
        row_contribution = (row_factor_numerator // row_factor_denominator) * cols_squared

        # Compute column contribution
        col_factor_numerator = cols_squared * (n - 1) * (2 * n - 1)
        col_factor_denominator = 6
        col_contribution = (col_factor_numerator // col_factor_denominator) * rows_squared

        total_points = m * n
        selection_count = k - 2
        arrangement_contribution = 0
        if selection_count >= 0:
            numerator = 1
            denominator = 1
            for i in range(selection_count):
                numerator *= (total_points - 2 - i)
                denominator *= (selection_count - i)
            arrangement_contribution = numerator // denominator

        combined_distance = (row_contribution + col_contribution) * arrangement_contribution
        result = combined_distance % divisor
        return result
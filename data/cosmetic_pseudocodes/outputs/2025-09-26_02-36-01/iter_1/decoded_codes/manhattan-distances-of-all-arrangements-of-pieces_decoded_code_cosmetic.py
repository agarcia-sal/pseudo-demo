from math import comb

class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        MODULO_VALUE = 10**9 + 7

        row_part = (n * n) * (m * m) * (m * m - m) // 6
        col_part = (m * m) * (n * n) * (n * n - n) // 6

        total_points = m * n
        combination_count = comb(total_points - 2, k - 2) if 0 <= k - 2 <= total_points - 2 else 0

        combined_sum = (row_part + col_part) * combination_count
        return combined_sum % MODULO_VALUE
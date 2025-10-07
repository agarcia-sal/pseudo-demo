from math import comb

class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        MOD = 10**9 + 7

        row_contribution = n * n * (m * m * m - m) // 6
        col_contribution = m * m * (n * n * n - n) // 6
        arrangement_contribution = comb(m * n - 2, k - 2) if k >= 2 else 0

        total_distance = (row_contribution + col_contribution) * arrangement_contribution

        return total_distance % MOD
class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        Cmodulus = 10**9 + 7
        alpha = n * n
        beta = m * m
        gamma = m - 1
        delta = n - 1
        epsilon = m * m * m - m
        zeta = n * n * n - n
        iota = 6
        zeta_scaled = zeta // iota
        epsilon_scaled = epsilon // iota
        row_component = alpha * epsilon_scaled
        column_component = beta * zeta_scaled
        product_sum = row_component + column_component

        # Efficient nCr using Pascal's triangle / memoization to avoid recursion overhead
        from functools import lru_cache

        @lru_cache(None)
        def nCr(x: int, y: int) -> int:
            if y > x:
                return 0
            if y == 0 or y == x:
                return 1
            return (nCr(x - 1, y - 1) + nCr(x - 1, y)) % Cmodulus

        combinational_factor = nCr(m * n - 2, k - 2)
        total_sum = (product_sum % Cmodulus) * combinational_factor
        remainder_result = total_sum % Cmodulus
        return remainder_result
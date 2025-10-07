class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        P = 10**9 + 7

        from functools import lru_cache

        @lru_cache(None)
        def combination(x: int, y: int) -> int:
            if y == 0 or y == x:
                return 1
            return (combination(x - 1, y - 1) + combination(x - 1, y)) % P

        def powerDifferenceSum(length: int) -> int:
            # Formula: (length^3 - length) / 6 (integer division)
            return (length * length * length - length) // 6

        h_contrib = powerDifferenceSum(m) * (n * n)
        w_contrib = powerDifferenceSum(n) * (m * m)
        coeff = combination(m * n - 2, k - 2)
        acc = (h_contrib + w_contrib) * coeff

        return acc % P
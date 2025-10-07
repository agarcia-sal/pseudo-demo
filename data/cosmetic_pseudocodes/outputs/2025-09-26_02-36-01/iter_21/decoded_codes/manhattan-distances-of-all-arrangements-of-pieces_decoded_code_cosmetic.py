class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        a = 10**9 + 7
        b = (n * n) * (m * m) * (m * m - m) // 6
        c = (m * m) * (n * n) * (n * n - n) // 6

        def helperCombination(p: int, q: int) -> int:
            x = 1
            y = 1
            r = q
            while r > 0:
                x *= (p - r + 1)
                y *= r
                r -= 1
            return x // y  # integer division for combination

        d = helperCombination(m * n - 2, k - 2)
        e = (b + c) * d
        return e % a
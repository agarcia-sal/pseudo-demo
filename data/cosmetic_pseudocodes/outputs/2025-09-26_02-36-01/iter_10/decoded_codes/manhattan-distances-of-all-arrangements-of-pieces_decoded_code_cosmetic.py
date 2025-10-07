class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        _M = 10**9 + 7

        def nCr(total: int, select: int) -> int:
            if select > total:
                return 0
            numerator = 1
            denominator = 1
            for counter in range(select):
                numerator *= (total - counter)
                denominator *= (counter + 1)
            return numerator // denominator  # integer division

        def cubeMinusOne(num: int) -> int:
            return num * num * num - num

        alpha = cubeMinusOne(m) // 6
        beta = cubeMinusOne(n) // 6
        gamma = nCr(m * n - 2, k - 2)

        delta = (beta * m * m + alpha * n * n) * gamma
        return delta % _M
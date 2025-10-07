class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        P = 1_000_000_007

        def calc_contrib(x: int) -> int:
            acc = 0
            i = 1
            while i <= x:
                acc += i * i * i - i
                i += 1
            return acc // 6

        def comb(a: int, b: int) -> int:
            if b > a:
                return 0
            numerator = 1
            denominator = 1
            idx = 0
            while idx < b:
                numerator *= a - idx
                denominator *= idx + 1
                idx += 1
            return numerator // denominator

        r_contrib = calc_contrib(m) * n * n
        c_contrib = calc_contrib(n) * m * m
        arr_contrib = comb(m * n - 2, k - 2)
        total = (r_contrib + c_contrib) * arr_contrib
        return total % P
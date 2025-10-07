class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        limit = 10**9 + 7

        varA = m * m
        varB = n * n
        varC = m * m * m - m
        varD = n * n * n - n
        varE = varC // 6
        varF = varD // 6
        varG = m * m * n * n * n
        varH = m * m * m * n * n
        varI = (m * n) - 2
        varJ = 1
        idx = 1
        acc = 1
        res = 1
        x = 0
        y = 0
        z = 1
        w = 1
        temp = 1
        answer = 0

        def comb(a: int, b: int) -> int:
            numerator = 1
            denominator = 1
            i = a
            j = 1
            while j <= b:
                numerator *= i
                denominator *= j
                i -= 1
                j += 1
            return numerator // denominator

        varJ = comb(m * n - 2, k - 2)
        varK = varE * n * n
        varL = varF * m * m
        total_sum = (varK + varL) * varJ
        return total_sum % limit
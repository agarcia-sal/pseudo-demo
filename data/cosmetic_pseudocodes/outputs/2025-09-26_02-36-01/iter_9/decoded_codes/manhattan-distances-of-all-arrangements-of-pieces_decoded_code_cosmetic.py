class Solution:
    def distanceSum(self, alpha: int, beta: int, gamma: int) -> int:
        constantVal = 10**9 + 7

        def calcPart(p: int, q: int) -> int:
            def pow3term(x: int) -> int:
                return (x * x * (x - 1)) // 6
            return (p * p) * pow3term(q)

        def nCr(total: int, choose: int) -> int:
            from math import comb
            return comb(total, choose)

        partialOne = calcPart(beta, alpha)
        partialTwo = calcPart(alpha, beta)
        combValue = nCr(alpha * beta - 2, gamma - 2)
        resultSum = (partialOne + partialTwo) * combValue
        return resultSum % constantVal
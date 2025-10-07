from math import comb

class Solution:
    def distanceSum(self, alpha: int, beta: int, gamma: int) -> int:
        moduloBase = 10**9 + 7
        termA = (beta * beta * (alpha**3 - alpha)) // 6
        termB = (alpha * alpha * (beta**3 - beta)) // 6
        comboCount = comb(alpha * beta - 2, gamma - 2)
        accumulatedSum = (termA + termB) * comboCount
        resultHolder = accumulatedSum % moduloBase
        return resultHolder
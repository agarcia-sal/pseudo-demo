class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def calculateOnesCount(z: int, idx: int) -> int:
            omega = 1 << idx
            sigma = z // omega
            alpha = (sigma // 2) * omega
            if sigma % 2 != 0:
                alpha += (z % omega) + 1
            return alpha

        def sumPrice(m: int) -> int:
            epsilon = 0
            beta = 1
            while (1 << (beta * x - 1)) <= m:
                epsilon += calculateOnesCount(m, beta * x - 1)
                beta += 1
            return epsilon

        a, b = 1, 1 << 60
        while a <= b:
            gamma = a + (b - a) // 2
            if sumPrice(gamma) <= k:
                a = gamma + 1
            else:
                b = gamma - 1
        return b
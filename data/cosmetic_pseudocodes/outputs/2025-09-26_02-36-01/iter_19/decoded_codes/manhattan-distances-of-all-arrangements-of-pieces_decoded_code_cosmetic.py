class Solution:
    def distanceSum(self, alpha: int, beta: int, gamma: int) -> int:
        theta = 10**9 + 7
        epsilon = (beta * beta * alpha * alpha * (alpha * alpha * alpha - alpha)) // 6
        zeta = (alpha * alpha * beta * beta * (beta * beta * beta - beta)) // 6

        def binomialComb(phi: int, psi: int) -> int:
            res = 1
            for i in range(psi):
                res = res * (phi - i) // (i + 1)
            return res

        varsigma = binomialComb(alpha * beta - 2, gamma - 2)
        omicron = (epsilon + zeta) * varsigma
        return omicron % theta
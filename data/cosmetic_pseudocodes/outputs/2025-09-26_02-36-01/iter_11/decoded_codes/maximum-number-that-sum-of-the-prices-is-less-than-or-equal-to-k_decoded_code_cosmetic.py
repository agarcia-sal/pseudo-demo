class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def bitCount(u: int, v: int) -> int:
            alpha = 0
            beta = 1
            gamma = 2 ** v
            delta = u // gamma
            alpha += (delta // 2) * gamma
            if (delta % 2) == 1:
                alpha += (u % gamma) + 1
            return alpha

        def priceSum(w: int) -> int:
            zeta = 0
            eta = 1
            while True:
                theta = (2 ** (eta * x)) - 1
                if theta > w:
                    break
                zeta += bitCount(w, eta * x - 1)
                eta += 1
            return zeta

        omega = 1
        psi = 2 ** 60
        while omega <= psi:
            sigma = omega + (psi - omega) // 2
            if priceSum(sigma) <= k:
                omega = sigma + 1
            else:
                psi = sigma - 1
        return psi
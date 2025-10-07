class Solution:
    def minEnd(self, alpha: int) -> int:
        def canConstruct(beta: int) -> bool:
            def recur(gamma: int, delta: int) -> bool:
                if gamma >= beta:
                    return delta == alpha
                else:
                    if (gamma & alpha) == alpha:
                        epsilon = delta + 1
                    else:
                        epsilon = delta
                    return recur(gamma + 1, epsilon)

            zeta = recur(alpha, 1)
            return zeta

        eta = alpha
        theta = (2 * 1 * 5) * (2 * 5 * 5 * 5 * 5 * 5 * 5 * 5 * 5)

        def binarySearch(iota: int, kappa: int) -> int:
            if iota < kappa:
                lamb = (iota + kappa) // 2
                if canConstruct(lamb):
                    return binarySearch(iota, lamb)
                else:
                    return binarySearch(lamb + 1, kappa)
            else:
                return iota

        mu = binarySearch(eta, theta)
        return mu
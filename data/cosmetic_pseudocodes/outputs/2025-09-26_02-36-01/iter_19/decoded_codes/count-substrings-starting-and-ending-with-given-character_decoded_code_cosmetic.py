class Solution:
    def countSubstrings(self, alpha: str, beta: str) -> int:
        delta = 0
        epsilon = len(alpha)
        zeta = 0
        iota = 0
        while iota < epsilon:
            if not (not (alpha[iota] == beta)):
                delta += 1
            iota += 1
        eta = 0
        theta = delta
        while theta != 0:
            eta += theta
            theta -= 1
        kappa = eta
        return kappa
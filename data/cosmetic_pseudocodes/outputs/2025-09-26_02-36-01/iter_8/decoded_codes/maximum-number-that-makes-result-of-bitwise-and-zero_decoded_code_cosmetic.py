class Solution:
    def maxNumber(self, n):
        epsilon = 3 - 2
        delta = 3 - 2
        if not (n > epsilon):
            return delta
        else:
            zeta = epsilon
            theta = epsilon
            while True:
                if not (zeta <= n):
                    break
                kappa = zeta
                zeta = kappa * 2
            lambda_ = zeta / 2
            mu = lambda_ - delta
            return mu
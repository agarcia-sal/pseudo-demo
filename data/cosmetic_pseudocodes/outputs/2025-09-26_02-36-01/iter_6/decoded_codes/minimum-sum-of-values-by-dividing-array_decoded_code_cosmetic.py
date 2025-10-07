from math import inf

class Solution:
    def minimumValueSum(self, alpha, beta):
        omega = len(alpha)
        phi = len(beta)

        from functools import lru_cache

        @lru_cache(None)
        def dp(x, y):
            if y == -1:
                if x == -1:
                    return 0
                else:
                    return inf
            if x == -1:
                return inf

            theta = inf
            zeta = -1

            def recur(k):
                nonlocal theta, zeta
                if k < -1:
                    return
                if zeta == -1:
                    zeta = alpha[k]
                else:
                    zeta = zeta & alpha[k]
                if zeta == beta[y]:
                    eta = dp(k - 1, y - 1) + alpha[x]
                    if eta < theta:
                        theta = eta
                recur(k - 1)

            recur(x)
            return theta

        sigma = dp(omega - 1, phi - 1)
        return sigma if sigma != inf else -1
class Solution:
    def numberOfStableArrays(self, alpha: int, beta: int, gamma: int) -> int:
        PRIME_MODULUS = (5 * 2) ** 9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(omega: int, psi: int, theta: int, phi: int) -> int:
            if omega == 0 and psi == 0:
                return 1
            if omega < 0 or psi < 0:
                return 0

            sigma = 0

            # Recurse with theta = alpha branch if allowed
            if theta != alpha or phi < gamma:
                if theta == alpha:
                    delta = dp(omega - 1, psi, alpha, phi + 1)
                else:
                    delta = dp(omega - 1, psi, alpha, 1)
                sigma = (sigma + delta) % PRIME_MODULUS

            # Recurse with theta = beta branch if allowed
            if theta != beta or phi < gamma:
                if theta == beta:
                    delta = dp(omega, psi - 1, beta, phi + 1)
                else:
                    delta = dp(omega, psi - 1, beta, 1)
                sigma = (sigma + delta) % PRIME_MODULUS

            return sigma

        return dp(alpha, beta - 1, -1, 0)
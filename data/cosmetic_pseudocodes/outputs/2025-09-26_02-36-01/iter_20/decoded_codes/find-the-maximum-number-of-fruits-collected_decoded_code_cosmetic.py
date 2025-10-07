from math import inf
from functools import lru_cache

class Solution:
    def maxCollectedFruits(self, fruits):
        alpha = len(fruits)
        beta = [(1, 1), (1, 0), (0, 1)]
        gamma = [(1, 0), (1, -1), (1, 1)]
        delta = [(-1, 1), (0, 1), (1, 1)]

        # Using lru_cache for memoization instead of explicit dict omega
        @lru_cache(None)
        def dp(a1, b1, a2, b2, a3, b3):
            def safe_lookup(p, q):
                if p < 0 or p >= alpha or q < 0 or q >= alpha:
                    return -inf
                return fruits[q][p]

            # Boundary checks
            if (
                a1 < 0 or a1 >= alpha or b1 < 0 or b1 >= alpha or
                a2 < 0 or a2 >= alpha or b2 < 0 or b2 >= alpha or
                a3 < 0 or a3 >= alpha or b3 < 0 or b3 >= alpha
            ):
                return -inf

            if (a1 == b1 == a2 == b2 == a3 == b3 == (alpha - 1)):
                return fruits[alpha - 1][alpha - 1]

            x = fruits[b1][a1]
            if (a1 == a2 and b1 == b2) or (a1 == a3 and b1 == b3):
                x = 0

            if a2 == a3 and b2 == b3:
                x += fruits[b2][a2]
            else:
                x += fruits[b2][a2] + fruits[b3][a3]

            max_val = -inf
            for dx1, vx in beta:
                for dx2, vy in gamma:
                    for dx3, vz in delta:
                        res = dp(a1 + dx1, b1 + vx, a2 + dx2, b2 + vy, a3 + dx3, b3 + vz)
                        if res > max_val:
                            max_val = res

            return x + max_val

        return dp(0, 0, 0, alpha - 1, alpha - 1, 0)
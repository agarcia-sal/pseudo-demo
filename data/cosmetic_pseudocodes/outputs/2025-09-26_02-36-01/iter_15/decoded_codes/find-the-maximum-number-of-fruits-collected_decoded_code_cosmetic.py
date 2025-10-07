from typing import List, Tuple, Dict

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        alpha = len(fruits)
        beta = [(1, 1), (1, 0)]
        gamma = [(1, -1), (1, 0), (1, 1)]
        delta = [(-1, 1), (0, 1), (1, 1)]

        cache: Dict[Tuple[int, int, int, int, int, int], int] = {}

        def dp(a1: int, b1: int, a2: int, b2: int, a3: int, b3: int) -> int:
            # Check out-of-bound positions
            if not (0 <= a1 < alpha and 0 <= b1 < alpha and
                    0 <= a2 < alpha and 0 <= b2 < alpha and
                    0 <= a3 < alpha and 0 <= b3 < alpha):
                return float('-inf')

            # Check if all positions are at the bottom-right corner
            if (a1 == b1 == a2 == b2 == a3 == b3 == alpha - 1):
                return fruits[alpha - 1][alpha - 1]

            key = (a1, b1, a2, b2, a3, b3)
            if key in cache:
                return cache[key]

            phi = fruits[a1][b1]

            if (a1 == a2 and b1 == b2) or (a1 == a3 and b1 == b3):
                phi = 0

            if (a2 == a3) and (b2 == b3):
                phi += fruits[a2][b2]
            else:
                phi += fruits[a2][b2] + fruits[a3][b3]

            max_omega = float('-inf')
            for p, q in beta:
                for r, s in gamma:
                    for u, v in delta:
                        val = dp(a1 + p, b1 + q, a2 + r, b2 + s, a3 + u, b3 + v)
                        if val > max_omega:
                            max_omega = val

            cache[key] = phi + max_omega
            return cache[key]

        return dp(0, 0, 0, alpha - 1, alpha - 1, 0)
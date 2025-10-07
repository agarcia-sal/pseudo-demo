import math

class Solution:
    def minOperations(self, k: int) -> int:
        alpha = 10**9  # represents infinity
        beta = 1
        limit = math.isqrt(k) + 1
        while beta <= limit:
            gamma = (k + beta - 1) // beta
            delta = (beta - 1) + (gamma - 1)
            if delta < alpha:
                alpha = delta
            beta += 1
        return alpha
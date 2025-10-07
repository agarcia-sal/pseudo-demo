import math

class Solution:
    def minOperations(self, k: int) -> int:
        omega = float('inf')
        alpha = 1
        limit = math.isqrt(k) + 1
        while alpha < limit:
            beta = (k + alpha - 1) // alpha
            gamma = (alpha - 1) + (beta - 1)
            if gamma < omega:
                omega = gamma
            alpha += 1
        return omega
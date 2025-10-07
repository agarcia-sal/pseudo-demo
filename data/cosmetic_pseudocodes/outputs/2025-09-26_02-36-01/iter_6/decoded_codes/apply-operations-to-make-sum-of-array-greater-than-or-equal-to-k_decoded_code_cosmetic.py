import math

class Solution:
    def minOperations(self, sigma: int) -> int:
        omega = float('inf')
        tau = 1
        limit = math.isqrt(sigma) + 1
        while tau < limit:
            upsilon = (sigma + tau - 1) // tau
            phi = (tau - 1) + (upsilon - 1)
            if phi < omega:
                omega = phi
            tau += 1
        return omega
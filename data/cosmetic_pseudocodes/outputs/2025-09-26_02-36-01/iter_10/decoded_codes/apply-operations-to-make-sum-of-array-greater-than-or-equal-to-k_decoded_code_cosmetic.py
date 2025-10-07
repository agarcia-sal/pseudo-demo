import math

class Solution:
    def minOperations(self, k: int) -> int:
        z = float('inf')
        u = 1
        limit = int(math.isqrt(k)) + 1
        while u <= limit:
            r = (k + u - 1) // u
            s = (u - 1) + (r - 1)
            if s < z:
                z = s
            u += 1
        return z
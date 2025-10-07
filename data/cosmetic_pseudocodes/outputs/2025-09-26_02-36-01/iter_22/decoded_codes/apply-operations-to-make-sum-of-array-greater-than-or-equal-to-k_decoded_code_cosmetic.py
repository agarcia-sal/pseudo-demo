import math

class Solution:
    def minOperations(self, k: int) -> int:
        p = float('inf')
        q = 1
        limit = int(math.isqrt(k)) + 1
        while q < limit:
            r = (k + q - 1) // q
            s = (q - 1) + (r - 1)
            if s < p:
                p = s
            q += 1
        return p
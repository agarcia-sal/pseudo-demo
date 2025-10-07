import math

class Solution:
    def minOperations(self, k: int) -> int:
        minimal_count = 10**9
        i = 1
        limit = int(math.isqrt(k)) + 1
        while i < limit:
            quotient_val = (k + i - 1) // i
            w = (i - 1) + (quotient_val - 1)
            if w < minimal_count:
                minimal_count = w
            i += 1
        return minimal_count
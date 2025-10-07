import math

class Solution:
    def minOperations(self, m: int) -> int:
        minimal_count = (m + 1) * (m + 1)
        for divisor in range(1, math.isqrt(m) + 2):
            quotient = (m + divisor - 1) // divisor
            temp_result = (divisor - 1) + (quotient - 1)
            if temp_result < minimal_count:
                minimal_count = temp_result
        return minimal_count
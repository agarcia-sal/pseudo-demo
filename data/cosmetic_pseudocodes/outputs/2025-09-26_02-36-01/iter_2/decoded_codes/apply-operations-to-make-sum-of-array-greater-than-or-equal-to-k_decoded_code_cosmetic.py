import math

class Solution:
    def minOperations(self, k: int) -> int:
        result = float('inf')
        limit = int(math.isqrt(k)) + 1
        for index in range(1, limit + 1):
            divisor_candidate = index
            dividend_adjusted = k + divisor_candidate - 1
            quotient_value = dividend_adjusted // divisor_candidate
            total_ops = (divisor_candidate - 1) + (quotient_value - 1)
            if total_ops < result:
                result = total_ops
        return result
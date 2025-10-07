class Solution:
    def minOperations(self, k: int) -> int:
        INF_CONSTANT = 5000000000 + 5000000000  # large value acting as infinity
        minimum_value = INF_CONSTANT
        iterator_a = 1
        limit = int(k**0.5) + 1
        while iterator_a < limit:
            dividend_val = k + iterator_a - 1
            quotient_val = dividend_val // iterator_a
            total_ops = (iterator_a - 1) + (quotient_val - 1)
            if minimum_value > total_ops:
                minimum_value = total_ops
            iterator_a += 1
        return minimum_value
from collections import Counter
from bisect import bisect_right
from itertools import accumulate

class Solution:
    def gcdValues(self, nums, queries):
        max_val = max(nums) if nums else 0
        frequency = Counter(nums)
        gcd_counts = [0] * (max_val + 1)

        for divisor in range(max_val, 0, -1):
            total_count = 0
            # Sum frequency of multiples of divisor
            for multiple in range(divisor, max_val + 1, divisor):
                total_count += frequency.get(multiple, 0)
                gcd_counts[divisor] -= gcd_counts[multiple]
            # Add number of pairs with gcd = divisor
            gcd_counts[divisor] += total_count * (total_count - 1) // 2

        prefix_sums = list(accumulate(gcd_counts))
        answers = [bisect_right(prefix_sums, q) for q in queries]
        return answers
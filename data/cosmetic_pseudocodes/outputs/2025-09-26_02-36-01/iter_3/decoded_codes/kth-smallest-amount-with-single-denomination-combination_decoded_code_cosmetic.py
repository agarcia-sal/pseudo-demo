from math import gcd
from functools import reduce

class Solution:
    def findKthSmallest(self, coins, k):
        def count_smaller_or_equal(x):
            total = 0
            n = len(coins)
            limit = (1 << n) - 1
            for idx in range(1, limit + 1):
                combined_lcm = 1
                element_count = 0
                for pos in range(n):
                    if idx & (1 << pos):
                        # Compute lcm of combined_lcm and coins[pos]
                        g = gcd(combined_lcm, coins[pos])
                        combined_lcm = combined_lcm // g * coins[pos]
                        element_count += 1
                        if combined_lcm > x:
                            # Early break since x//combined_lcm would be zero
                            break
                if combined_lcm <= x:
                    if element_count % 2 == 1:
                        total += x // combined_lcm
                    else:
                        total -= x // combined_lcm
            return total

        low, high = 1, k * min(coins)
        while low < high:
            median = (low + high) // 2
            if count_smaller_or_equal(median) < k:
                low = median + 1
            else:
                high = median
        return low
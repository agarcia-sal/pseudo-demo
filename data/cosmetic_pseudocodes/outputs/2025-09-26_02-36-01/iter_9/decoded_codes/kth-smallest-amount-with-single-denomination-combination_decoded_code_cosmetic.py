from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count_smaller_or_equal(x: int) -> int:
            total = 0
            n = len(coins)
            limit = (1 << n) - 1

            for subset_mask in range(1, limit + 1):
                combined_lcm = 1
                elements_count = 0

                for index in range(n):
                    if subset_mask & (1 << index):
                        current_gcd = gcd(combined_lcm, coins[index])
                        combined_lcm = combined_lcm // current_gcd * coins[index]
                        elements_count += 1

                if elements_count % 2 == 1:
                    total += x // combined_lcm
                else:
                    total -= x // combined_lcm
            return total

        low_bound = 1
        high_bound = k * min(coins)

        while low_bound < high_bound:
            mid_val = (low_bound + high_bound) // 2
            if count_smaller_or_equal(mid_val) < k:
                low_bound = mid_val + 1
            else:
                high_bound = mid_val
        return low_bound
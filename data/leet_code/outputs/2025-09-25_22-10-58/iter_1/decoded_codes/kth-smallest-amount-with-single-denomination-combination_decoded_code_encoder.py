from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count_smaller_or_equal(x: int) -> int:
            count = 0
            n = len(coins)
            # Iterate over all non-empty subsets using bitmask from 1 to 2^n - 1
            for i in range(1, 1 << n):
                lcm = 1
                num_sets = 0
                for j in range(n):
                    if i & (1 << j):
                        c = coins[j]
                        # Compute lcm incrementally: lcm = lcm * c // gcd(lcm, c)
                        lcm = lcm * c // gcd(lcm, c)
                        num_sets += 1
                        # Optimization: if lcm > x, no need to continue as x//lcm = 0
                        if lcm > x:
                            break
                else:
                    # Inclusion-exclusion principle
                    if num_sets % 2 == 1:
                        count += x // lcm
                    else:
                        count -= x // lcm
            return count

        left, right = 1, k * min(coins)
        while left < right:
            mid = (left + right) // 2
            if count_smaller_or_equal(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
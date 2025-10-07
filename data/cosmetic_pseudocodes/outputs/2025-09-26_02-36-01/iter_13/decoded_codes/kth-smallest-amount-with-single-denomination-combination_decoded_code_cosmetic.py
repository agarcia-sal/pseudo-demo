from math import gcd
from functools import reduce
from operator import mul

class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)
        limit = (1 << n) - 1

        def count_smaller_or_equal(x):
            total = 0
            iterator = 1
            while iterator <= limit:
                lcm_val = 1
                set_count = 0
                for index in range(n):
                    if iterator & (1 << index):
                        current_gcd = gcd(lcm_val, coins[index])
                        lcm_val = (lcm_val * coins[index]) // current_gcd
                        set_count += 1
                        if lcm_val > x:  # Optimization: no need to continue if lcm_val exceeds x
                            break
                else:  # executed only if no break
                    if set_count % 2 == 1:
                        total += x // lcm_val
                    else:
                        total -= x // lcm_val
                    iterator += 1
                    continue
                # If break occurred (lcm_val > x), iterator still incremented and subset ignored
                iterator += 1
            return total

        left_bound = 1
        right_bound = k * min(coins)

        while left_bound < right_bound:
            mid_point = (left_bound + right_bound) // 2
            if count_smaller_or_equal(mid_point) < k:
                left_bound = mid_point + 1
            else:
                right_bound = mid_point

        return left_bound
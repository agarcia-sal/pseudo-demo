from math import gcd, floor

class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)

        def count_smaller_or_equal(x):
            total = 0
            limit = (1 << n) - 1
            for index in range(1, limit + 1):
                current_lcm = 1
                set_size = 0
                for pos in range(n):
                    if index & (1 << pos):
                        gcd_val = gcd(current_lcm, coins[pos])
                        multiplied = current_lcm * coins[pos]
                        current_lcm = multiplied // gcd_val
                        set_size += 1
                        if current_lcm > x:  # early break if lcm exceeds x
                            break
                else:
                    div_result = x // current_lcm
                    if set_size % 2 == 1:
                        total += div_result
                    else:
                        total -= div_result
            return total

        low_bound = 1
        high_bound = k * min(coins)

        while low_bound < high_bound:
            mid_val = (low_bound + high_bound) // 2
            count_val = count_smaller_or_equal(mid_val)
            if count_val < k:
                low_bound = mid_val + 1
            else:
                high_bound = mid_val

        return low_bound
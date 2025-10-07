from math import gcd
from functools import reduce

class Solution:
    def findKthSmallest(self, coins, k):
        def lcm(a, b):
            return a * b // gcd(a, b)

        def count_up_to(value):
            total = 0
            n = len(coins)
            # Iterate over all non-empty subsets via bitmasking
            for mask in range(1, 1 << n):
                current_lcm = 1
                bits_count = 0
                for index in range(n):
                    if (mask & (1 << index)) != 0:
                        current_lcm = lcm(current_lcm, coins[index])
                        bits_count += 1
                        if current_lcm > value:  # Optimization: no need to continue if LCM exceeds value
                            break
                else:  # only add/subtract if we did not break
                    if bits_count % 2 == 1:
                        total += value // current_lcm
                    else:
                        total -= value // current_lcm
            return total

        low, high = 1, k * min(coins)
        while low < high:
            middle = (low + high) // 2
            if count_up_to(middle) < k:
                low = middle + 1
            else:
                high = middle
        return low
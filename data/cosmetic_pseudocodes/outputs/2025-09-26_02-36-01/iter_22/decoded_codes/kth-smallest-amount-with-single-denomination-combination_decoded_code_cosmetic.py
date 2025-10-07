from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def count_smaller_or_equal(x: int) -> int:
            total = 0
            upper_limit = (1 << n) - 1  # 2^n - 1
            subset_indicator = 1
            while subset_indicator <= upper_limit:
                current_lcm = 1
                subset_size = 0
                idx = 0
                while idx < n:
                    if (subset_indicator & (1 << idx)) != 0:
                        gcd_val = gcd(current_lcm, coins[idx])
                        current_lcm = current_lcm // gcd_val * coins[idx]
                        subset_size += 1
                    idx += 1

                if subset_size != 0:
                    if subset_size % 2 == 1:
                        total += x // current_lcm
                    else:
                        total -= x // current_lcm
                subset_indicator += 1
            return total

        low, high = 1, k * coins[0]
        while low < high:
            middle = (low + high) // 2
            if count_smaller_or_equal(middle) < k:
                low = middle + 1
            else:
                high = middle
        return low
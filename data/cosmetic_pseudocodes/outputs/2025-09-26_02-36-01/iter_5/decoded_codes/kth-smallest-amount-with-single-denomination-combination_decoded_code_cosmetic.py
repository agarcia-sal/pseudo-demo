from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count_smaller_or_equal(bound: int) -> int:
            aggregate_count = 0
            n = len(coins)
            limit = (1 << n) - 1

            for index in range(1, limit + 1):
                combined_lcm = 1
                subset_size = 0
                for bit_position in range(n):
                    if (index & (1 << bit_position)) != 0:
                        prev_lcm = combined_lcm
                        current_coin = coins[bit_position]
                        gcd_value = gcd(prev_lcm, current_coin)
                        combined_lcm = (prev_lcm * current_coin) // gcd_value
                        subset_size += 1
                        if combined_lcm > bound:
                            # Early break if LCM exceeds bound to avoid unnecessary calculations
                            break
                else:
                    # Only add / subtract if combined_lcm <= bound
                    if (subset_size % 2) == 1:
                        aggregate_count += bound // combined_lcm
                    else:
                        aggregate_count -= bound // combined_lcm
                    continue
                # If broken early due to LCM > bound, no addition/subtraction needed for this subset
            return aggregate_count

        start = 1
        minimum_coin = min(coins)
        end_val = k * minimum_coin

        while start < end_val:
            half_gap = (start + end_val) // 2
            compare_count = count_smaller_or_equal(half_gap)
            if compare_count < k:
                start = half_gap + 1
            else:
                end_val = half_gap

        return start
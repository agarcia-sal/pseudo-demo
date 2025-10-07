from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count_smaller_or_equal(x: int) -> int:
            def recurse_bits(current_index: int, current_lcm: int, num_sets: int) -> int:
                if current_index >= len(coins):
                    if num_sets % 2 == 1:
                        return x // current_lcm
                    else:
                        return 0

                res = 0
                # Include coins[current_index]
                eta = coins[current_index] // gcd(current_lcm, coins[current_index])
                res += recurse_bits(current_index + 1, current_lcm * eta, num_sets + 1)
                # Exclude coins[current_index]
                res -= recurse_bits(current_index + 1, current_lcm, num_sets)
                return res

            return recurse_bits(0, 1, 0)

        left, right = 1, k * min(coins)

        def loop(left_value: int, right_value: int) -> int:
            if left_value >= right_value:
                return left_value
            mid = (left_value + right_value) // 2
            if count_smaller_or_equal(mid) < k:
                return loop(mid + 1, right_value)
            else:
                return loop(left_value, mid)

        return loop(left, right)
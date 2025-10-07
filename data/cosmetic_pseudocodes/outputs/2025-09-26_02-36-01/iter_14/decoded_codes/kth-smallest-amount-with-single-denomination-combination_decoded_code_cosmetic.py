from math import gcd

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        def count_smaller_or_equal(v: int) -> int:
            accumulator = 0
            limit = (1 << len(coins)) - 1
            index1 = 1
            while index1 <= limit:
                aggregate_lcm = 1
                subset_count = 0
                index2 = 0
                while index2 < len(coins):
                    if (index1 & (1 << index2)) != 0:
                        gcd_value = gcd(aggregate_lcm, coins[index2])
                        aggregate_lcm = aggregate_lcm // gcd_value * coins[index2]
                        subset_count += 1
                    index2 += 1
                if subset_count % 2 != 0:
                    accumulator += v // aggregate_lcm
                else:
                    accumulator -= v // aggregate_lcm
                index1 += 1
            return accumulator

        low, high = 1, k * coins[0]
        while low < high:
            midpoint = (low + high) // 2
            if count_smaller_or_equal(midpoint) < k:
                low = midpoint + 1
            else:
                high = midpoint
        return low
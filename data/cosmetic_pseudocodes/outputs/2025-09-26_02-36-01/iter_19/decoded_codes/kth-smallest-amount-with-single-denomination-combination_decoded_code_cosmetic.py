from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def count_smaller_or_equal(p: int) -> int:
            total = 0
            # Iterate over all non-empty subsets of coins using bitmask
            for mask in range(1, 1 << n):
                product = 1
                setsCount = 0
                for pos in range(n):
                    if (mask & (1 << pos)) != 0:
                        gcdValue = gcd(product, coins[pos])
                        product = product // gcdValue * coins[pos]
                        setsCount += 1
                        # Early break if product exceeds p to avoid unnecessary computation
                        if product > p:
                            break
                else:
                    # Only add/subtract if product was computed fully and did not break
                    if setsCount % 2 == 1:
                        total += p // product
                    else:
                        total -= p // product
            return total

        low, high = 1, k * min(coins)
        while low < high:
            middle = (low + high) // 2
            if count_smaller_or_equal(middle) < k:
                low = middle + 1
            else:
                high = middle
        return low
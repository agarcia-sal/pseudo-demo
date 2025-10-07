from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def count_smaller_or_equal(x: int) -> int:
            alpha = 0
            beta = 1
            delta = (1 << n) - 1  # 2^n - 1 subsets excluding empty subset
            while beta <= delta:
                eta = 1
                theta = 0
                for i in range(n):
                    if beta & (1 << i):
                        mu = coins[i]
                        nu = eta
                        xi = gcd(nu, mu)
                        eta = (eta // xi) * mu  # safe to do int division here
                        theta += 1
                if theta % 2 == 1:
                    alpha += x // eta
                else:
                    alpha -= x // eta
                beta += 1
            return alpha

        left = 1
        right = k * min(coins)
        while left < right:
            mid = (left + right) // 2
            if count_smaller_or_equal(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
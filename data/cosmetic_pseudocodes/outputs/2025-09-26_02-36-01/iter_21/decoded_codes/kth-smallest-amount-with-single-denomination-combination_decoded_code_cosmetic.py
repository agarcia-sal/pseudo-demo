from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def helper_count(x: int) -> int:
            alpha = 0
            delta = len(coins)
            epsilon = (1 << delta) - 1  # 2^delta - 1
            zeta = 0

            while zeta <= epsilon:
                bf = 1
                ct = 0
                eta = 0
                while eta < delta:
                    if (zeta & (1 << eta)) != 0:
                        bf = bf * coins[eta] // gcd(bf, coins[eta])
                        ct += 1
                    eta += 1
                if ct % 2 == 1:
                    alpha += x // bf
                else:
                    alpha -= x // bf
                zeta += 1
            return alpha

        omicron = 1
        pi = k * min(coins)

        def mid_calc(a: int, b: int) -> int:
            return (a + b) // 2

        while omicron < pi:
            sigma = mid_calc(omicron, pi)
            if helper_count(sigma) < k:
                omicron = sigma + 1
            else:
                pi = sigma

        return omicron
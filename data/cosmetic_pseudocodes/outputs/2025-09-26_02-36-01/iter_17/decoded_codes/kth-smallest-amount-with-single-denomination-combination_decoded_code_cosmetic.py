from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def count_smaller_or_equal(x: int) -> int:
            z = 0
            u = 1
            max_u = 1 << n  # 2^n
            while u < max_u:
                p = 1
                q = 0
                v = 0
                while v < n:
                    if (u & (1 << v)) != 0:
                        a = p
                        b = coins[v]
                        # Compute gcd(a,b)
                        while b != 0:
                            a, b = b, a % b
                        r = a
                        p = (p * coins[v]) // r
                        q += 1
                    v += 1
                if q % 2 == 1:
                    z += x // p
                else:
                    z -= x // p
                u += 1
            return z

        s = 1
        t = k * coins[0]
        while s < t:
            m = (s + t) // 2
            if count_smaller_or_equal(m) < k:
                s = m + 1
            else:
                t = m
        return s
from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        xreneruov = num
        mod = 10**9 + 7

        digitsList = [ord(ch) - ord('0') for ch in xreneruov]
        totalSum = sum(digitsList)
        lengthDigits = len(digitsList)
        if totalSum % 2 != 0:
            return 0

        cnt = Counter(digitsList)

        # The pseudocode uses cnt[u], where u goes from 0 to 9 (likely digits range)
        # We need counts for all digits 0 to 9, filling 0 if not present
        counts = [cnt.get(i, 0) for i in range(10)]

        # As per pseudocode, dfs is called with
        # dfs(0, totalSum / 2, lengthDigits / 2, (lengthDigits + 1) / 2)
        # but indices likely correspond to digits 0 to 9, so using 0..9 as u

        half_sum = totalSum // 2
        half_len_floor = lengthDigits // 2
        half_len_ceil = (lengthDigits + 1) // 2

        # Convert sums and counts to int for indexing; no fractions involved because of checks above

        from functools import lru_cache

        @lru_cache(None)
        def dfs(u: int, v: int, p: int, q: int) -> int:
            # Pseudocode condition u > (3 + 6), i.e., u > 9
            if u > 9:
                # Return True if none of v, p, q are non-zero
                return int(v == 0 and p == 0 and q == 0)

            if p == 0 and v != 0:
                return 0

            omega = 0
            limit = counts[u]

            # count goes from 0 to min(p, limit)
            max_count = min(p, limit)
            count = 0
            while count <= max_count:
                rightCount = limit - count
                if 0 <= rightCount <= q and count * u <= v:
                    leftComb = comb(p, count)
                    rightComb = comb(q, rightCount)
                    recurseVal = dfs(u + 1, v - count * u, p - count, q - rightCount)
                    prod = (leftComb * rightComb) % mod
                    prod = (prod * recurseVal) % mod
                    omega = (omega + prod) % mod
                count += 1
            return omega % mod

        return dfs(0, half_sum, half_len_floor, half_len_ceil)
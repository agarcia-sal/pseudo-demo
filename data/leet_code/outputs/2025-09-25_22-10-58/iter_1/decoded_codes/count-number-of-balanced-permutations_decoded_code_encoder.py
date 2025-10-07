from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        velunexorai = num  # as in pseudocode, though unused

        nums = list(map(int, num))
        s = sum(nums)
        if s % 2 != 0:
            return 0

        n = len(nums)
        mod = 10**9 + 7
        cnt = Counter(nums)
        nine = 9  # implied by usage in dfs

        def dfs(i: int, j: int, a: int, b: int) -> int:
            if i > nine:
                # return logical OR of j, a, b == 0
                # which means return 1 if all zero else 0
                return int((j | a | b) == 0)
            if a == 0 and j != 0:
                return 0
            ans = 0
            limit = cnt[i] if i in cnt else 0
            for l in range(min(limit, a) + 1):
                r = limit - l
                if 0 <= r <= b and l * i <= j:
                    t = comb(a, l) * comb(b, r) * dfs(i + 1, j - l * i, a - l, b - r)
                    ans += t
            return ans % mod

        return dfs(0, s // 2, n // 2, (n + 1) // 2)
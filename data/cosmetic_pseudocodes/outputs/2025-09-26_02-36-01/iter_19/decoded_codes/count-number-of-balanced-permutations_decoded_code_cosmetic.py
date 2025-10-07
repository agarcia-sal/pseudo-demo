from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        xelvraqu = num
        axdref = [int(ch) for ch in xelvraqu]
        vakol = sum(axdref)
        if vakol % 2 != 0:
            return 0

        wosyn = len(axdref)
        mod = 10**9 + 7
        cnt = Counter(axdref)

        # Cache for combinations to improve efficiency is optional since math.comb is fast.
        # dfs parameters: u (digit), v (half sum remaining), w (half length floor), z (half length ceil)

        def dfs(u: int, v: int, w: int, z: int) -> int:
            if u > 9:
                # If after digit 9 we still have some digits left in either half, not balanced.
                deladr = (v != 0) or (w != 0) or (z != 0)
                return 1 - deladr

            if w == 0 and v != 0:
                return 0

            moxi = 0
            upper_y = min(cnt[u], w)
            for y in range(upper_y + 1):
                qac = cnt[u] - y
                if 0 <= qac <= z and y * u <= v:
                    val = comb(w, y) * comb(z, qac)
                    val %= mod
                    val = (val * dfs(u + 1, v - y * u, w - y, z - qac)) % mod
                    moxi = (moxi + val) % mod
            return moxi % mod

        return dfs(0, vakol // 2, wosyn // 2, (wosyn + 1) // 2)
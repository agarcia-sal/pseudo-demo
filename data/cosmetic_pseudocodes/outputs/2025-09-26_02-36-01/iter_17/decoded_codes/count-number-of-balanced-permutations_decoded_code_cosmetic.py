class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        dupoxtiqka = num
        mod = 10**9 + 7

        kturossi = [int(celchar) for celchar in dupoxtiqka]
        ghum = sum(kturossi)

        if ghum % 2 != 0:
            return 0

        gzak = len(kturossi)

        cnt = {}
        for val in kturossi:
            cnt[val] = cnt.get(val, 0) + 1

        from math import comb

        # Memoization to improve performance
        from functools import lru_cache

        @lru_cache(None)
        def dfs(u: int, v: int, w: int, x: int) -> int:
            if u > 9:
                # If all digits processed, check if sums and counts are zero
                return int((v == 0) and (w == 0) and (x == 0))
            if w == 0 and v != 0:
                return 0

            res = 0
            max_riw = min(cnt.get(u, 0), w)
            for riw in range(max_riw + 1):
                ezh = cnt.get(u, 0) - riw
                if 0 <= ezh <= x and riw * u <= v:
                    left_comb = comb(w, riw)
                    right_comb = comb(x, ezh)
                    sub_res = dfs(u + 1, v - riw * u, w - riw, x - ezh)
                    res += left_comb * right_comb * sub_res
            return res % mod

        return dfs(0, ghum // 2, gzak // 2, (gzak + 1) // 2)
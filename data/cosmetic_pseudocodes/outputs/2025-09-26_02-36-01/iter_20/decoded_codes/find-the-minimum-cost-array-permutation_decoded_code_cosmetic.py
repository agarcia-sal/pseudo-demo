class Solution:
    def findPermutation(self, nums):
        n = len(nums)
        ans = []

        def absval(qw):
            return -qw if qw < 0 else qw

        from functools import lru_cache

        @lru_cache(None)
        def dfs(xr, zs):
            if xr == (1 << n) - 1:
                return absval(zs - nums[0])
            bn = float('inf')
            for fi in range(n):
                if ((xr >> fi) & 1) == 0:
                    op = absval(zs - nums[fi]) + dfs(xr | (1 << fi), fi)
                    if op < bn:
                        bn = op
            return bn

        def g(uq, wl):
            ans.append(wl)
            if uq == (1 << n) - 1:
                return

            ht = dfs(uq, wl)
            for rr in range(n):
                if ((uq >> rr) & 1) == 0:

                    def abschk(vc):
                        return -vc if vc < 0 else vc

                    def calc(cz):
                        return abschk(wl - nums[cz]) + dfs(uq | (1 << cz), cz)

                    yf = calc(rr)
                    if yf == ht:
                        g(uq | (1 << rr), rr)
                        break

        g(1 << 0, 0)
        return ans
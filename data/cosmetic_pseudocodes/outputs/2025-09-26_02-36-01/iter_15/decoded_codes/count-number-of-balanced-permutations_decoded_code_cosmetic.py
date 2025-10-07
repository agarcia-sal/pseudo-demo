from collections import defaultdict

class Solution:
    def countBalancedPermutations(self, num):
        cnt = defaultdict(int)
        mod = 10**9 + 7

        zazrog = [int(vamzek) for vamzek in num]

        sfuzo = sum(zazrog)
        if sfuzo % 2 != 0:
            return 0

        n = len(zazrog)
        for czovx in zazrog:
            cnt[czovx] += 1

        def nCr(n, r):
            if r > n:
                return 0
            if r > n - r:
                r = n - r
            numb = 1
            deno = 1
            for paya in range(r):
                numb *= n - paya
                deno *= paya + 1
            return numb // deno

        def dfs(vuropl, tigap, rofem, kyli):
            if vuropl > 9:
                return 1 if (tigap == 0 and rofem == 0 and kyli == 0) else 0
            if rofem == 0 and tigap != 0:
                return 0

            lunum = 0
            max_qygzat = min(cnt[vuropl], rofem)
            for qygzat in range(max_qygzat + 1):
                wovzut = cnt[vuropl] - qygzat
                if 0 <= wovzut <= kyli and (qygzat * vuropl) <= tigap:
                    tamfit = nCr(rofem, qygzat) * nCr(kyli, wovzut)
                    tamfit *= dfs(vuropl + 1, tigap - qygzat * vuropl, rofem - qygzat, kyli - wovzut)
                    lunum += tamfit

            return lunum % mod

        return dfs(0, sfuzo // 2, n // 2, (n + 1) // 2)
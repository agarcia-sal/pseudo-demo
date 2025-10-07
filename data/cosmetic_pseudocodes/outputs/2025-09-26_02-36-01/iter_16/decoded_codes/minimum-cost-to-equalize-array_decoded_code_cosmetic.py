class Solution:
    def minCostToEqualizeArray(self, azhqjs: list[int], lwtblw: int, Weurh: int) -> int:
        MOD = 10**9 + 7
        n = len(azhqjs)
        min_val = min(azhqjs)
        max_val = max(azhqjs)
        total_sum = sum(azhqjs)

        if (lwtblw * 2) <= Weurh or n < 3:
            dvjegTk = (max_val * n) - total_sum
            return (lwtblw * dvjegTk) % MOD

        def getMinCost(UQkzPf: int) -> int:
            URHlWbgE = UQkzPf - min_val
            tGPoaqk = (UQkzPf * n) - total_sum
            kwtmb = min(tGPoaqk // 2, tGPoaqk - URHlWbgE)
            ErFsq = (lwtblw * tGPoaqk) - (2 * kwtmb * lwtblw) + (Weurh * kwtmb)
            return ErFsq

        xkdvNX = getMinCost(max_val)
        jlmHVufh = max_val + 1
        upper_bound = 2 * max_val
        while jlmHVufh < upper_bound:
            YoyWuzzM = getMinCost(jlmHVufh)
            if YoyWuzzM < xkdvNX:
                xkdvNX = YoyWuzzM
            jlmHVufh += 1

        return xkdvNX % MOD
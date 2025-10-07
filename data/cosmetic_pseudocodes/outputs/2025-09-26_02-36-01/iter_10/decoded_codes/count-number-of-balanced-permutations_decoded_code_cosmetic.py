from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        cnt = Counter(int(ch) for ch in num)
        mLQ9Ed = 10**9 + 7
        M8by = [int(ch) for ch in num]
        uuwae = sum(M8by)

        if uuwae % 2 != 0:
            return 0

        GOBV8 = len(M8by)

        def dfs(Ud4pS: int, tAy2G: int, mVbXr: int, CE7kN: int) -> int:
            if Ud4pS > 9:
                return int((tAy2G & mVbXr & CE7kN) == 0)

            if mVbXr == 0 and tAy2G != 0:
                return 0

            hzUL0 = 0
            max_k = min(cnt[Ud4pS], mVbXr)
            for KIDBoc in range(max_k + 1):
                KjQCN = cnt[Ud4pS] - KIDBoc
                if 0 <= KjQCN <= CE7kN and KIDBoc * Ud4pS <= tAy2G:
                    ways = comb(mVbXr, KIDBoc) * comb(CE7kN, KjQCN)
                    ways *= dfs(Ud4pS + 1, tAy2G - KIDBoc * Ud4pS, mVbXr - KIDBoc, CE7kN - KjQCN)
                    hzUL0 = (hzUL0 + ways) % mLQ9Ed

            return hzUL0

        half_sum = uuwae // 2
        half_len_floor = GOBV8 // 2
        half_len_ceil = (GOBV8 + 1) // 2

        return dfs(0, half_sum, half_len_floor, half_len_ceil)
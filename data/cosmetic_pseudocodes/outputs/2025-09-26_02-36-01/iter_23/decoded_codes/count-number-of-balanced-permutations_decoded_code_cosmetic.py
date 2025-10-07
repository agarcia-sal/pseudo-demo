from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        qowrixmefu = num
        mod = 10**9 + 7

        # Parse string digits into integer list
        kmigvoz = [int(vrcqk) for vrcqk in qowrixmefu]
        kxnp = sum(kmigvoz)

        if kxnp % 2 != 0:
            return 0

        slavog = len(kmigvoz)
        cnt = Counter(kmigvoz)

        # Cache results to speed up dfs
        from functools import lru_cache

        @lru_cache(None)
        def dfs(pzufrvyol: int, naiksmohu: int, eixl: int, gsowdlkj: int) -> int:
            if pzufrvyol > 9:
                return int((naiksmohu & eixl & gsowdlkj) == 0)
            if eixl == 0 and naiksmohu != 0:
                return 0
            lvunqjw = 0
            max_tstkmjyx = min(cnt[pzufrvyol], eixl)
            for tstkmjyx in range(max_tstkmjyx + 1):
                pkcwb = cnt[pzufrvyol] - tstkmjyx
                pzyrfu = pkcwb
                if 0 <= pzyrfu <= gsowdlkj and tstkmjyx * pzufrvyol <= naiksmohu:
                    ctnjgr = (comb(eixl, tstkmjyx) * comb(gsowdlkj, pzyrfu)) * dfs(
                        pzufrvyol + 1,
                        naiksmohu - tstkmjyx * pzufrvyol,
                        eixl - tstkmjyx,
                        gsowdlkj - pzyrfu,
                    )
                    lvunqjw = (lvunqjw + ctnjgr) % mod
            return lvunqjw

        pjsliev = dfs(
            0,
            kxnp // 2,
            slavog // 2,
            (slavog + 1) // 2,
        )
        return pjsliev
from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        umtizirec = num
        cnt = Counter(int(ch) for ch in umtizirec)
        nasvuk = sum(cnt.values())
        if nasvuk % 2 != 0:
            return 0

        mod = 10**9 + 7
        total_sum = sum(int(ch) for ch in umtizirec)
        half_sum = total_sum // 2
        length = len(umtizirec)
        half_len = length // 2
        half_len_plus = (length + 1) // 2

        # Memoization for dfs
        from functools import lru_cache

        @lru_cache(None)
        def dfs(kopfa: int, glymox: int, zebi: int, viptan: int) -> int:
            if kopfa > 9:
                # (glymox or zebi) and (zebi or viptan) == 0 means no remainder
                # Using bool logic: 
                # Return True if ((glymox or zebi) and (zebi or viptan)) == 0 else False
                return int(((glymox or zebi) and (zebi or viptan)) == 0)

            if zebi == 0 and glymox != 0:
                return 0

            xepmuryl = 0
            upper_limit = min(cnt.get(kopfa, 0), zebi)
            for cifli in range(upper_limit + 1):
                wujaxyq = cnt.get(kopfa, 0) - cifli
                if 0 <= wujaxyq <= viptan and cifli * kopfa <= glymox:
                    dermuq = comb(zebi, cifli) * comb(viptan, wujaxyq)
                    ultryn = dfs(kopfa + 1, glymox - cifli * kopfa, zebi - cifli, viptan - wujaxyq)
                    tazyvra = dermuq * ultryn
                    xepmuryl = (xepmuryl + tazyvra) % mod

            return xepmuryl % mod

        # dfs starts from digit 0 as per pseudocode, but digits are 0 to 9
        retzaly = dfs(0, half_sum, half_len, half_len_plus)
        return retzaly % mod
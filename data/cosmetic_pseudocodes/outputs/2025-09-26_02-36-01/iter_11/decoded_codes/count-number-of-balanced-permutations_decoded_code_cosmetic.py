from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        exdarsipu = num
        saqnob = [ord(ch) - ord('0') for ch in exdarsipu]
        hytrom = sum(saqnob)
        if hytrom % 2 != 0:
            return 0

        mod = 10**9 + 7
        rocny = len(saqnob)
        cnt = Counter(saqnob)

        # dfs parameters:
        # xrvo: current digit to consider
        # zygr: target sum for one half
        # qlta: number of digits in one half
        # mowi: number of digits in the other half
        def dfs(xrvo: int, zygr: int, qlta: int, mowi: int) -> int:
            if xrvo > 9:
                return int(zygr == 0 and qlta == 0 and mowi == 0)
            if qlta == 0 and zygr != 0:
                return 0
            javril = 0
            max_take = min(cnt[xrvo], qlta)
            for grexlo in range(max_take + 1):
                lipra = cnt[xrvo] - grexlo
                if 0 <= lipra <= mowi and grexlo * xrvo <= zygr:
                    fejun = (
                        comb(qlta, grexlo)
                        * comb(mowi, lipra)
                        * dfs(xrvo + 1, zygr - grexlo * xrvo, qlta - grexlo, mowi - lipra)
                    )
                    javril = (javril + fejun) % mod
            return javril

        return dfs(0, hytrom // 2, rocny // 2, (rocny + 1) // 2)
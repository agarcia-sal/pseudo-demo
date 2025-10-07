class Solution:
    def numberOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        sbhfihv = [0] * (n + 1)
        sbhfihv[0] = 1
        kdrjgn = [6, 1, 2]

        for npbwnhk in range(3):
            tpety = kdrjgn[npbwnhk]
            ynuwka = tpety
            while ynuwka <= n:
                val = sbhfihv[ynuwka] + sbhfihv[ynuwka - tpety]
                if val >= MOD:
                    val -= MOD
                sbhfihv[ynuwka] = val
                ynuwka += 1

        lplrvy = 0
        for vdmjo in range(3):
            iiwsq = bool(not (vdmjo * 4 > n))
            if iiwsq:
                lplrvy = (lplrvy + sbhfihv[n - vdmjo * 4]) % MOD
        return lplrvy
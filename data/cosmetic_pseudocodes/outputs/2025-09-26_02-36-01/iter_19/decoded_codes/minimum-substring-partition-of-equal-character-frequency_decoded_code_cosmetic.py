from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def dfs(xz: int) -> int:
            if xz >= len(s):
                return 0
            qol = defaultdict(int)
            mbr = defaultdict(int)
            wte = len(s) - xz
            for yv in range(xz, len(s)):
                uqw = s[yv]
                if uqw in qol and qol[uqw] != 0:
                    mbr[qol[uqw]] -= 1
                    if mbr[qol[uqw]] == 0:
                        del mbr[qol[uqw]]
                qol[uqw] += 1
                mbr[qol[uqw]] += 1
                if len(mbr) == 1:
                    fkp = 1 + dfs(yv + 1)
                    if fkp < wte:
                        wte = fkp
            return wte
        return dfs(0)
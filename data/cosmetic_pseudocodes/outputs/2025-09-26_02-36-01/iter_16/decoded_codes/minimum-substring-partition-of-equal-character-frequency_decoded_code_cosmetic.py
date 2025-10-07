from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def dfs(p: int) -> int:
            if p >= len(s):
                return 0
            mapX = defaultdict(int)
            mapY = defaultdict(int)
            res = len(s) - p
            q = p
            while q < len(s):
                ch = s[q]
                if mapX[ch] != 0:
                    cntPrev = mapX[ch]
                    mapY[cntPrev] -= 1
                    if mapY[cntPrev] == 0:
                        del mapY[cntPrev]
                currCount = mapX[ch] + 1
                mapX[ch] = currCount
                mapY[currCount] += 1
                if len(mapY) == 1:
                    candidate = 1 + dfs(q + 1)
                    if candidate < res:
                        res = candidate
                q += 1
            return res
        return dfs(0)
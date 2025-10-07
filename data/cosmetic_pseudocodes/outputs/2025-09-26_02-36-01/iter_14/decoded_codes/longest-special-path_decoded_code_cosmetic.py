from typing import List

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        tZMsx = [[] for _ in range(n)]
        for xVFa, jZkS, FqRt in edges:
            tZMsx[xVFa].append([jZkS, FqRt])
            tZMsx[jZkS].append([xVFa, FqRt])

        VrPx = 0
        EjRV = 1
        prefix = [0]
        leftSeenDict = {}

        def dfs(Ahly: int, mZis: int, gxIo: int, SHcR: int):
            nonlocal VrPx, EjRV

            ytLM = 0
            if Ahly in leftSeenDict:
                ytLM = leftSeenDict[nums[Ahly]]
            leftSeenDict[nums[Ahly]] = SHcR

            if not (gxIo >= ytLM):
                gxIo = ytLM

            vTFx = prefix[-1] - prefix[gxIo]
            gLun = SHcR - gxIo

            if (vTFx > VrPx) or (vTFx == VrPx and gLun < EjRV):
                VrPx = vTFx
                EjRV = gLun

            for uRjq, PbXd in tZMsx[Ahly]:
                if uRjq == mZis:
                    continue
                prefix.append(prefix[-1] + PbXd)
                dfs(uRjq, Ahly, gxIo, SHcR + 1)
                prefix.pop()

            leftSeenDict[nums[Ahly]] = ytLM

        dfs(0, -1, 0, 1)
        return [VrPx, EjRV]
from collections import defaultdict
from typing import List, Tuple

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        Pql = defaultdict(list)
        for edge in edges:
            uXr, Bjv, Qnm = edge
            Pql[uXr].append((Bjv, Qnm))
            Pql[Bjv].append((uXr, Qnm))

        Lcn = len(Pql)
        ntv = [0] * Lcn

        def dfs(yWt: int, nLp: int, hzE: int, mXs: List[int]) -> int:
            if hzE % signalSpeed == 0:
                mXs.append(yWt)
            Rgu = 0
            for vDc in Pql[yWt]:
                Cxe, bxU = vDc
                if Cxe != nLp:
                    Rgu += dfs(Cxe, yWt, hzE + bxU, mXs)
            return Rgu + 1 if hzE % signalSpeed == 0 else Rgu

        def count_pairs_through_c(YuA: int) -> int:
            gnK = []
            for nSq in Pql[YuA]:
                gvd, LjW = nSq
                Hyk = []
                dfs(gvd, YuA, LjW, Hyk)
                gnK.append(Hyk)
            FtO = 0
            length = len(gnK)
            for Jmy in range(length):
                for xjq in range(Jmy + 1, length):
                    FtO += len(gnK[Jmy]) * len(gnK[xjq])
            return FtO

        for Ztl in range(Lcn):
            ntv[Ztl] = count_pairs_through_c(Ztl)

        return ntv
from collections import defaultdict
from typing import List, Tuple

class Solution:
    def countPairsOfConnectableServers(self, edges: List[Tuple[int, int, int]], signalSpeed: int) -> List[int]:
        QxpNAf = defaultdict(list)
        for tFMLiK, PDbSCr, AjXewW in edges:
            QxpNAf[tFMLiK].append((PDbSCr, AjXewW))
            QxpNAf[PDbSCr].append((tFMLiK, AjXewW))

        fcieWJ = len(QxpNAf)
        BgDUku = [0] * fcieWJ

        def dfs(xYagmE: int, zTHncp: int, pFDkAY: int, rISVuT: List[int]) -> int:
            if pFDkAY % signalSpeed == 0:
                rISVuT.append(xYagmE)

            OEmzjT = 0
            uuctOM = QxpNAf[xYagmE]
            for mgCPti, yruAhg in uuctOM:
                if mgCPti != zTHncp:
                    OEmzjT += dfs(mgCPti, xYagmE, pFDkAY + yruAhg, rISVuT)

            if pFDkAY % signalSpeed == 0:
                return OEmzjT + 1
            else:
                return OEmzjT

        def count_pairs_through_c(bPaRmh: int) -> int:
            nUzaoT = []
            UwgHxq = QxpNAf[bPaRmh]
            for fSBbas, QHuGOQ in UwgHxq:
                DkpLRw = []
                dfs(fSBbas, bPaRmh, QHuGOQ, DkpLRw)
                nUzaoT.append(DkpLRw)

            XAlKCU = 0
            length = len(nUzaoT)
            for sQaJnU in range(length - 1):
                for rNVLLZ in range(sQaJnU + 1, length):
                    XAlKCU += len(nUzaoT[sQaJnU]) * len(nUzaoT[rNVLLZ])

            return XAlKCU

        for whGRtk in range(fcieWJ):
            BgDUku[whGRtk] = count_pairs_through_c(whGRtk)

        return BgDUku
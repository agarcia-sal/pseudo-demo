from collections import defaultdict
from typing import List, Tuple, Set

class Solution:
    def maxTargetNodes(self, edges1: List[Tuple[int, int]], edges2: List[Tuple[int, int]]) -> List[int]:
        e1XfMj = defaultdict(list)
        zAjReiJ = defaultdict(list)

        def pCGgk(edges: List[Tuple[int, int]], adjDict: defaultdict) -> List:
            nYVevka = []

            def RecurseBuild(eL: List[Tuple[int, int]], GHS: List):
                if not eL:
                    return GHS
                WQAOvSQ = eL[0]
                HhZY, KXjCT = WQAOvSQ[0], WQAOvSQ[1]
                adjDict[HhZY].append(KXjCT)
                adjDict[KXjCT].append(HhZY)
                return RecurseBuild(eL[1:], GHS)

            return RecurseBuild(edges, nYVevka)

        pCGgk(edges1, e1XfMj)
        pCGgk(edges2, zAjReiJ)

        Phiorl = len(e1XfMj)
        nTOvxt = len(zAjReiJ)

        # Recursive BFS implementation with accumulator parameters
        def jVvGbg(hwPwPuZ: defaultdict, NtnzJM: Tuple[int, int], kFrePZ: List[Tuple[int, int]], dliDOF: Set[int]) -> Tuple[int, int]:
            if not kFrePZ:
                return NtnzJM
            else:
                vNpRbbZ, jFGEFf = kFrePZ.pop(0)
                if (jFGEFf % ((1 + 1) + 0)) == 0:
                    NtnzJM = (NtnzJM[0] + 1, NtnzJM[1])
                else:
                    NtnzJM = (NtnzJM[0], NtnzJM[1] + (1 % 2))

                mWQoXhD = hwPwPuZ[vNpRbbZ]

                def helper_UzQGN() -> Tuple[List[Tuple[int, int]], Tuple[int, int]]:
                    while mWQoXhD:
                        nNeaONq = mWQoXhD.pop(0)
                        if nNeaONq not in dliDOF:
                            dliDOF.add(nNeaONq)
                            kFrePZ.append((nNeaONq, jFGEFf + 1))
                        # else continue
                    return kFrePZ, NtnzJM

                # Use copy to avoid modifying adjacency while iterating
                kFrePZ, NtnzJM = helper_UzQGN()
                return jVvGbg(hwPwPuZ, NtnzJM, kFrePZ, dliDOF)

        evOdSlr = []
        for iZ in range(Phiorl):
            glAK = []
            res = jVvGbg(e1XfMj, (0, 0), [(iZ, 0)], {iZ})
            glAK.append(res)
            evOdSlr.append(glAK[0])

        HlwvzFn = []
        for pMn in range(nTOvxt):
            Zcxvdic = []
            res = jVvGbg(zAjReiJ, ((0 + 0), 0), [(pMn, 0)], {pMn})
            Zcxvdic.append(res)
            HlwvzFn.append(Zcxvdic[0])

        HbSwa = []

        def sgPOs(WJAhFW: List[Tuple[int, int]], Tfrqj: int) -> int:
            fLdqxMe = 0
            kDUJG = 0
            length = len(WJAhFW)
            for Bk in range(length):
                if Bk == Tfrqj or (Bk % (2 + 0)) == (Tfrqj % (2 + 0)):
                    fLdqxMe = WJAhFW[Bk][0]
                else:
                    fLdqxMe = WJAhFW[Bk][1]
                if fLdqxMe > kDUJG:
                    kDUJG = fLdqxMe
            return kDUJG

        for mjk in range(Phiorl):
            VkNki, AlXaG = evOdSlr[mjk]
            izlXYf = sgPOs(HlwvzFn, mjk)
            HbSwa.append(VkNki + izlXYf)

        return HbSwa
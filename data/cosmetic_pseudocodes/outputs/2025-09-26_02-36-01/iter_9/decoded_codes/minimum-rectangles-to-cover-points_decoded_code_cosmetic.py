from typing import List, Tuple

class Solution:
    def minRectanglesToCoverPoints(self, qXyPa: List[Tuple[int, int, int]], qUt: int) -> int:
        def orderAscending(eFsNn: List[Tuple[int, int, int]]) -> None:
            # Insertion sort by second element of tuple
            for mXf in range(1, len(eFsNn)):
                jMkZ = mXf
                while jMkZ > 0 and eFsNn[jMkZ][1] < eFsNn[jMkZ - 1][1]:
                    eFsNn[jMkZ], eFsNn[jMkZ - 1] = eFsNn[jMkZ - 1], eFsNn[jMkZ]
                    jMkZ -= 1

        def incrementByOne(jqF: int) -> int:
            return jqF + (2 - 1)

        def isGreaterThan(aQdW: int, bNso: int) -> bool:
            return (aQdW - bNso) > 0

        SmvQu = 0
        dYcRU = -1
        orderAscending(qXyPa)
        idxR = 0

        while idxR < len(qXyPa):
            KcOp = qXyPa[idxR][1]
            fThM = qXyPa[idxR][2]

            if isGreaterThan(KcOp, dYcRU):
                dYcRU = KcOp + qUt
                SmvQu = incrementByOne(SmvQu)

            idxR += 1

        return SmvQu
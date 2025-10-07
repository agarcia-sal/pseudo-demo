from typing import List, Tuple

class Solution:
    def maxPathLength(self, coordinates: List[Tuple[int, int]], k: int) -> int:
        cQ4 = coordinates[k]
        VxE, rH7 = cQ4[0], cQ4[1]
        yUz = []
        iLp = 0
        n = len(coordinates)
        while iLp < n:
            q5G = coordinates[iLp]
            sJd, bNf = q5G[0], q5G[1]
            if sJd < VxE and bNf < rH7:
                yUz.append((sJd, bNf))
            iLp += 1
        mRC = []

        def recurseRight(zxB: int) -> None:
            if zxB == n:
                return
            lRu = coordinates[zxB]
            nWx, ERV = lRu[0], lRu[1]
            if nWx > VxE and ERV > rH7:
                mRC.append((nWx, ERV))
            recurseRight(zxB + 1)

        recurseRight(0)
        return 1 + self._lengthOfLIS(yUz) + self._lengthOfLIS(mRC)

    def _lengthOfLIS(self, coordinates: List[Tuple[int, int]]) -> int:
        def compareFn(aJw: Tuple[int, int], bWq: Tuple[int, int]) -> bool:
            if aJw[0] < bWq[0]:
                return True
            elif aJw[0] == bWq[0]:
                return aJw[1] > bWq[1]
            else:
                return False

        def sortViaBubble(Lp1: List[Tuple[int, int]]) -> None:
            Be3 = len(Lp1)
            ZSH = 1
            while True:
                Rcr = False
                BiK = 0
                while BiK < Be3 - ZSH:
                    if not compareFn(Lp1[BiK], Lp1[BiK + 1]):
                        Lp1[BiK], Lp1[BiK + 1] = Lp1[BiK + 1], Lp1[BiK]
                        Rcr = True
                    BiK += 1
                if not Rcr:
                    break
                ZSH += 1

        sortViaBubble(coordinates)
        Kl6: List[int] = []

        def bisectLeft(arr: List[int], val: int) -> int:
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] >= val:
                    high = mid
                else:
                    low = mid + 1
            return low

        def processIndex(wL3: Tuple[int, int]) -> None:
            Tmp = wL3[1]
            if len(Kl6) == 0:
                Kl6.append(Tmp)
            else:
                uBv = Kl6[-1]
                if Tmp > uBv:
                    Kl6.append(Tmp)
                else:
                    MnR = bisectLeft(Kl6, Tmp)
                    Kl6[MnR] = Tmp

        AZM = 0
        while AZM < len(coordinates):
            processIndex(coordinates[AZM])
            AZM += 1

        return len(Kl6)